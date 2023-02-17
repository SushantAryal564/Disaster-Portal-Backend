from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import Polygon
from django.contrib.gis.geos import fromstr
from django.contrib.gis.geos import GEOSGeometry
from .models import *

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.contrib.gis.gdal import SpatialReference, CoordTransform
from django.db import connection


class BufferPolygonIntersectionView(APIView):
    def get(self, request):
        print('gettin buildings.... wait')
        print("********************")
        lat = float(request.GET.get('lat'))
        lng = float(request.GET.get('lon'))
        buffer_distance = float(request.GET.get('buffer_distance'))
        p4326=Point(lng, lat, srid=4326)
        print('lat long sent',lng,lat)
        print('lat long got',p4326)
        ct = CoordTransform(SpatialReference(4326), SpatialReference(3857))
        p3857 = p4326.transform(ct, clone=True)
        # buffer_polygon_3857 = p3857.buffer(buffer_distance/100000)
        # buffer_polygon_4326 = p4326.buffer(buffer_distance/100000)
        
        print('Point transformned---->>>>>>',p4326) 
        query = """
  SELECT * FROM "Buildings"
WHERE ST_Intersects(
  geom,
  ST_Transform(
    ST_MakeEnvelope(85.28460208092133, 27.606122394532917, 85.35535620512481, 27.69326664414035, 4326),
    4326
  )
)  AND
  ST_DWithin(
    ST_Transform(
      ST_SetSRID(
        ST_Point(%s, %s),
        4326
      ),
      4326
    ),
    ST_Transform(geom, 4326),
    %s
  )
LIMIT 10000;
"""
        with connection.cursor() as cursor:
            cursor.execute("EXPLAIN ANALYZE " + query, [p4326.x, p4326.y,buffer_distance])
            explain_result = cursor.fetchall()
            print("Query plan:")
            for plan in explain_result:
                print(plan)
            
            cursor.execute(query , [p4326.x, p4326.y,buffer_distance])
            rows = cursor.fetchall()

        buildings = [] 
        for row in rows:
            way_wkb = row[1]
            osm_id=row[0]
            classes=row[4]
            name = row[5]
            type = row[6]            
            way_geometry = GEOSGeometry(way_wkb) 
            buildings.append([way_geometry,osm_id,classes,name,type])
                
        features = []
        for building in buildings:
          
            geos_polygon = building[0]
            osm_id=building[1]
            classes = building[2]
            name = building[3]
            type = building[4]
            
            feature = {
                "type": "Feature",
                "geometry":json.loads(geos_polygon.geojson),
                "properties": {"osm_id":osm_id,"classes":building[2],"name":building[3],"type":building[4]}
            }
            features.append(feature)
        
        feature_collection = {
            "type": "FeatureCollection",
            "features": features
        }
        return Response(feature_collection)
    
    
    
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import Polygon
from django.contrib.gis.measure import D
from django.http import JsonResponse
from django.views import View
import json
class BufferPolygonView(View):
    def get(self, request, *args, **kwargs):
        lat = float(request.GET.get('lat'))
        lon = float(request.GET.get('lon'))
        buffer_distance = float(request.GET.get('buffer_distance'))
        point = Point(lon, lat, srid=4326)
        buffer_polygon = point.buffer(buffer_distance/100000)
        polygon_geojson = {
            'type': 'Feature',
            'geometry': json.loads(buffer_polygon.geojson),
            'properties': {
                'point': [lon, lat],
                'buffer_distance': buffer_distance,
            }
        }

        return JsonResponse(polygon_geojson)