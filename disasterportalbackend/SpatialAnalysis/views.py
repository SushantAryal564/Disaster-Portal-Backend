from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import Polygon
from django.contrib.gis.geos import fromstr
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.contrib.gis.gdal import SpatialReference, CoordTransform
from django.db import connection
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework  import filters as rest_filters
from .models import *
import json

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


#trigger alertAPI view
from disasterApp.models import DisasterEvent
class BufferPolygonIntersectionViewBuildingTriggerAlert(APIView):
  def post(self, request):
      # pass
          lat = float(request.data['lat'])
          print("---------------------------------------------------",request.data['lat'])
          disaster_id = int(request.data['lat'])
          
          message = request.data['message']
          
          ob=DisasterEvent.objects.get(id=disaster_id)
          
          name=ob.name
          des=ob.description
          message=message+"/n"+name+des
          lng = request.data['lng']
          buffer_distance = float(request.data['buf'])/100000
          
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
          emails=[]
          print(
              'hjgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg',emails
          )
          # testemails=['cecilghimire@gmail.com','cecilghimire0@gmail.com']
          for row in rows:
              # print(row,"ROW")
              if row[11]:
                emails.append(row[11])  
          print(
              'hjgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg',emails
          )          
          import smtplib
          subject = 'LMC Disaster Alert'
          server = smtplib.SMTP('smtp.gmail.com', 587) 
          # message = 'Message you want to send'
          email_from = 'lalitpurmetro30@gmail.com'
          server.ehlo()
          server.starttls()
          for i in emails:

            server.login(email_from, "doomelyvemmsxteg")
            server.sendmail(email_from, i, message)  
                      # recipient_list = testemails
          # send_mail(subject, message, email_from, recipient_list)        
          return Response(emails)


from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class NearestAmenities(APIView):
    def get(self, request, latitude, longitude, distance=30):
        # Create a point object from the given latitude and longitude
        location = Point(float(longitude), float(latitude), srid=4326)
        
        # Query the Amenities model for the nearest amenities within the given distance
        nearest_amenities = Amenities.objects.filter(geom__distance_lte=(location, distance)).annotate(distance=Distance('geom', location)).order_by('distance')
        
        # Serialize the nearest amenities
        serializer = AmenitiesSerializer(nearest_amenities, many=True)
        
        # Return the serialized data as a JSON response
        return Response(serializer.data, status=status.HTTP_200_OK)

class NearestBuildings(APIView):
    def get(self, request, latitude, longitude, distance=30):
        # Create a point object from the given latitude and longitude
        location = Point(float(longitude), float(latitude), srid=4326)
        
        # Query the Buildings model for buildings within the given distance
        buildings = Buildings.objects.filter(geom__distance_lte=(location, distance))
        
        # Serialize the buildings
        serializer = BuildingsSerializer(buildings, many=True)
        
        # Return the serialized data as a JSON response
        return Response(serializer.data, status=status.HTTP_200_OK)
      
class NearestForests(APIView):
    def get(self, request, latitude, longitude, distance=30):
        location = Point(float(longitude), float(latitude), srid=4326)
        forests = Forest.objects.filter(geom__distance_lte=(location, distance))
        serializer = ForestSerializer(forests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class NearestRoads(APIView):
    def get(self, request, latitude, longitude, distance=30):
        location = Point(float(longitude), float(latitude), srid=4326)
        roads = Road.objects.filter(geom__distance_lte=(location, distance))
        serializer = RoadSerializer(roads, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class NearestWaterBody(APIView):
    def get(self, request, latitude, longitude, distance=30):
        location = Point(float(longitude), float(latitude), srid=4326)
        waterbodies = Waterbody.objects.filter(geom__distance_lte=(location, distance))
        serializer = WaterBodySerializer(waterbodies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
from rest_framework.pagination import PageNumberPagination

class MyPaginationClass(PageNumberPagination):
    page_size = 100 # number of items to return per page
    page_size_query_param = 'page_size'
    max_page_size = 1000
    
class BuildingViewset(viewsets.ModelViewSet):
    queryset = Buildings.objects.all()
    serializer_class = BuildingsSerializer
    # pagination_class = MyPaginationClass

    def get_queryset(self):
      queryset = super().get_queryset()
      ward = self.request.query_params.get('ward', None)
      if ward is not None:
          queryset = queryset.filter(ward=ward)
      return queryset
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)




from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['PATCH'])
def building_partial_update(request):
    osm_id = request.data.get('osm_id')
    qs = Buildings.objects.filter(osm_id=osm_id).first()
    if qs is None:
        return Response({"error": f"No Buildings object found for osm_id {osm_id}"}, status=400)
    ser = BuildingsSerializer(data=request.data, instance=qs, partial=True)
    if ser.is_valid():
        ser.save()
        return Response({"message": "Data updated successfully", "data": ser.data}, status=200)
    return Response({"error": ser.errors}, status=400)
    
class SingleBuildingViewset(APIView):

    queryset = Buildings.objects.all()
    serializer_class = BuildingsSerializer
    def get(self, request, *args, **kwargs):
        id=request.GET.get('id')
        if id is None:
            return Response(data={"msg":"no id"},status=400)
        queryset = Buildings.objects.filter(osm_id=id)[0]
        serialz=BuildingsSerializer(queryset)
        return Response(serialz.data)
        

class AmenitiesViewset(viewsets.ModelViewSet):
    queryset = Amenities.objects.all()
    serializer_class = AmenitiesSerializer
    def list(self, request, *args, **kwargs):
        tag= request.GET.get('tag');
        queryset= Amenities.objects.filter(fclass=tag)
        serializer = AmenitiesSerializer(queryset, many=True)
        return Response(serializer.data)
    
import geopandas as gpd
import psycopg2,os,shutil

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="disaster3",
    user="cecil3",
    password="cecil3"
)

from django.http import Http404, HttpResponse
@api_view(['GET'])
def download_building_event(request):
    ward = request.query_params.get('ward', None)
    dir = f'media/analysis_download/{ward}/'
    root_dir = f'media/analysis_download/'
    os.makedirs(dir, exist_ok=True)

    # # Establish a connection to the PostgreSQL database
    # conn = psycopg2.connect(
    #     host="localhost",
    #     database="mydatabase",
    #     user="myusername",
    #     password="mypassword"
    # )

    # Define the SQL query to select the data you want to read
    sql = f"""SELECT name,fclass,gid,geom FROM "Buildings" WHERE ward={ward} LIMIT 100"""

    # Use geopandas to read the data from the PostgreSQL database 
    gdf = gpd.read_postgis(sql, conn)

    # Close the database connection
   

    # Create the directory for the output file if it does not exist
    os.makedirs(dir, exist_ok=True)

    # Save the geopandas dataframe as a shapefile
    filename = "buildings.shp" 
    gdf.to_file(os.path.join(dir, filename), driver='ESRI Shapefile')

    # Create the zipfile for the output directory
    shutil.make_archive(base_name=root_dir+ward, format='zip', root_dir=root_dir, base_dir=ward)

    # Open the saved zipfile and read the contents into a response object
    with open(root_dir+ward+'.zip', 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename="{ward}.zip"'

    # Remove the output directory
    shutil.rmtree(dir)

    # Return the response object
    return response

@api_view(['GET'])

def download_disaster_event(request):
    # Get the fromdate and todate from the query parameters
    fromdate = request.query_params.get('fromdate')
    todate = request.query_params.get('todate')

    # Construct the SQL query to select all columns from the "disasterApp_disasterevent" table where date_event is within the date range
    sql = f"""SELECT id,geom,lat,long FROM "disasterApp_disasterevent" WHERE date_event BETWEEN '{fromdate}' AND '{todate}'"""

    # Set the directory to create a new folder called devent with date range in the name
    dir = f'media/analysis_download/devent_{fromdate}_to_{todate}/'
    root_dir = 'media/analysis_download/'
    os.makedirs(dir, exist_ok=True)


    # Use geopandas to read the data from the PostgreSQL database 
    gdf = gpd.read_postgis(sql, conn)

    # Close the database connection
 

    # Create the directory for the output file if it does not exist
    os.makedirs(dir, exist_ok=True)

    # Save the geopandas dataframe as a shapefile
    filename = f"devent_{fromdate}_to_{todate}.shp" 
    # gdf = gdf.drop(columns=['attributes'])
    gdf.to_file(os.path.join(dir, filename),
              driver='ESRI Shapefile')
    
    # Create the zipfile for the output directory
    shutil.make_archive(base_name=root_dir+f'devent_{fromdate}_to_{todate}', format='zip', root_dir=root_dir, base_dir=f'devent_{fromdate}_to_{todate}')

    # Open the saved zipfile and read the contents into a response object
    with open(root_dir+f'devent_{fromdate}_to_{todate}.zip', 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename="devent_{fromdate}_to_{todate}.zip"'

    # Remove the output directory
    shutil.rmtree(dir)

    # Return the response object
    return response