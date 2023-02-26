from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import Polygon
from django.contrib.gis.geos import fromstr
from django.contrib.gis.geos import GEOSGeometry
from .models import *
import json
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.contrib.gis.gdal import SpatialReference, CoordTransform
from django.db import connection



class BufferPolygonIntersectionViewBuilding(APIView):
  def get(self, request):
          lat = float(request.GET.get('lat'))
          lng = float(request.GET.get('lon'))
          buffer_distance = float(request.GET.get('buffer_distance'))/100000
          p4326=Point(lng, lat, srid=4326)
          print('lat long sent',lng,lat)
          print('lat long got',p4326)
          ct = CoordTransform(SpatialReference(4326), SpatialReference(3857))
          p3857 = p4326.transform(ct, clone=True)
          
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
    );
  """
          with connection.cursor() as cursor:
              cursor.execute("EXPLAIN ANALYZE " + query, [p4326.x, p4326.y,buffer_distance])
              explain_result = cursor.fetchall()
              print("Query plan:")
              for plan in explain_result:
                  print(plan)
              cursor.execute(query , [p4326.x, p4326.y,buffer_distance])
              rows = cursor.fetchall()
          features = [] 
          for row in rows:
              way_wkb = row[6]
              id=row[0]
              classes=row[3]
              name = row[4]
              osm_id = row[1]            
              way_geometry = GEOSGeometry(way_wkb) 
              features.append([way_geometry,id,classes,name,osm_id])
          buildings = []
          for building in features:
              geos_polygon = building[0]
              id=building[1]
              classes = building[2]
              name = building[3]
              osm_id = building[4]
              feature = {
                  "type": "Feature",
                  "geometry":json.loads(geos_polygon.geojson),
                  "properties": {"id":id,"classes":classes,"name":name,"osm_id":osm_id}
              }
              buildings.append(feature)
          feature_collection = {
              "type": "FeatureCollection",
              "features": buildings
          }
          return Response(feature_collection)

class BufferPolygonIntersectionViewForest(APIView):
    def get(self, request):
        print('gettin features.... wait')
        print("********************")
        lat = float(request.GET.get('lat'))
        lng = float(request.GET.get('lon'))
        buffer_distance = float(request.GET.get('buffer_distance'))/100000
        p4326=Point(lng, lat, srid=4326)
        print('lat long sent',lng,lat)
        print('lat long got',p4326)
        ct = CoordTransform(SpatialReference(4326), SpatialReference(3857))
        p3857 = p4326.transform(ct, clone=True)
        
        query = """
  SELECT * FROM "Forest"
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
  );
"""
        with connection.cursor() as cursor:
            cursor.execute("EXPLAIN ANALYZE " + query, [p4326.x, p4326.y,buffer_distance])
            explain_result = cursor.fetchall()
            print("Query plan:")
            for plan in explain_result:
                print(plan)
            cursor.execute(query , [p4326.x, p4326.y,buffer_distance])
            rows = cursor.fetchall()

        features = [] 
        for row in rows:
            way_wkb = row[5]
            id=row[0]
            classes=row[3]
            name = row[4]
            osm_id = row[1]            
            way_geometry = GEOSGeometry(way_wkb) 
            features.append([way_geometry,id,classes,name,osm_id])
        Forests = []
        for forest in features:
            geos_polygon = forest[0]
            id=forest[1]
            classes = forest[2]
            name = forest[3]
            osm_id = forest[4]
            feature = {
                "type": "Feature",
                "geometry":json.loads(geos_polygon.geojson),
                "properties": {"id":id,"classes":classes,"name":name,"osm_id":osm_id}
            }
            Forests.append(feature)
        feature_collection = {
            "type": "FeatureCollection",
            "features": Forests
        }
        return Response(feature_collection)

class BufferPolygonIntersectionViewWaterBody(APIView):
    def get(self, request):
        print('gettin features.... wait')
        print("********************")
        lat = float(request.GET.get('lat'))
        lng = float(request.GET.get('lon'))
        buffer_distance = float(request.GET.get('buffer_distance'))/100000
        p4326=Point(lng, lat, srid=4326)
        print('lat long sent',lng,lat)
        print('lat long got',p4326)
        ct = CoordTransform(SpatialReference(4326), SpatialReference(3857))
        p3857 = p4326.transform(ct, clone=True)
        
        query = """
  SELECT * FROM "Waterbody"
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
  );
"""
        with connection.cursor() as cursor:
            cursor.execute("EXPLAIN ANALYZE " + query, [p4326.x, p4326.y,buffer_distance])
            explain_result = cursor.fetchall()
            print("Query plan:")
            for plan in explain_result:
                print(plan)
            cursor.execute(query , [p4326.x, p4326.y,buffer_distance])
            rows = cursor.fetchall()

        features = [] 
        for row in rows:
            way_wkb = row[5]
            id=row[0]
            classes=row[3]
            name = row[4]
            osm_id = row[1]            
            way_geometry = GEOSGeometry(way_wkb) 
            features.append([way_geometry,id,classes,name,osm_id])
        Waterbodies = []
        for waterbody in features:
            geos_polygon = waterbody[0]
            id=waterbody[1]
            classes = waterbody[2]
            name = waterbody[3]
            osm_id = waterbody[4]
            feature = {
                "type": "Feature",
                "geometry":json.loads(geos_polygon.geojson),
                "properties": {"id":id,"classes":classes,"name":name,"osm_id":osm_id}
            }
            Waterbodies.append(feature)
        feature_collection = {
            "type": "FeatureCollection",
            "features": Waterbodies
        }
        return Response(feature_collection)

class BufferPolygonIntersectionViewAmenities(APIView):
    def get(self, request):
        print('gettin features.... wait')
        print("********************")
        lat = float(request.GET.get('lat'))
        lng = float(request.GET.get('lon'))
        buffer_distance = float(request.GET.get('buffer_distance'))/100000
        p4326=Point(lng, lat, srid=4326)
        print('lat long sent',lng,lat)
        print('lat long got',p4326)
        ct = CoordTransform(SpatialReference(4326), SpatialReference(3857))
        p3857 = p4326.transform(ct, clone=True)
        
        query = """
  SELECT * FROM "Amenities"
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
  );
"""
        with connection.cursor() as cursor:
            cursor.execute("EXPLAIN ANALYZE " + query, [p4326.x, p4326.y,buffer_distance])
            explain_result = cursor.fetchall()
            print("Query plan:")
            for plan in explain_result:
                print(plan)
            cursor.execute(query , [p4326.x, p4326.y,buffer_distance])
            rows = cursor.fetchall()

        features = [] 
        for row in rows:
            way_wkb = row[5]
            id=row[0]
            classes=row[3]
            name = row[4]
            osm_id = row[1]            
            way_geometry = GEOSGeometry(way_wkb) 
            features.append([way_geometry,id,classes,name,osm_id])
        Amenities = []
        for aminity in features:
            geos_polygon = aminity[0]
            id=aminity[1]
            classes = aminity[2]
            name = aminity[3]
            osm_id = aminity[4]
            feature = {
                "type": "Feature",
                "geometry":json.loads(geos_polygon.geojson),
                "properties": {"id":id,"classes":classes,"name":name,"osm_id":osm_id}
            }
            Amenities.append(feature)
        feature_collection = {
            "type": "FeatureCollection",
            "features": Amenities
        }
        return Response(feature_collection)

from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Amenities
from .serializers import AmenitiesSerializer

class NearestAmenities(APIView):
    def get(self, request, latitude, longitude):
        # Create a point object from the given latitude and longitude
        location = Point(float(longitude), float(latitude), srid=4326)
        
        # Query the Amenities model for the nearest amenities within 30 meters
        nearest_amenities = Amenities.objects.filter(geom__distance_lte=(location, 30)).annotate(distance=Distance('geom', location)).order_by('distance')
        
        # Serialize the nearest amenities
        serializer = AmenitiesSerializer(nearest_amenities, many=True)
        
        # Return the serialized data as a JSON response
        return Response(serializer.data, status=status.HTTP_200_OK)

class NearestBuildings(APIView):
    def get(self, request, latitude, longitude):
        location = Point(float(longitude), float(latitude), srid=4326)
        nearest_buildings = Buildings.objects.filter(geom__distance_lte=(location, 30)).annotate(distance=Distance('geom', location)).order_by('distance')
        serializer = AmenitiesSerializer(nearest_buildings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)