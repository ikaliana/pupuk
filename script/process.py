from osgeo import gdal
import sys
import psycopg2
import psycopg2.extras

conn = None
try:
	conn = psycopg2.connect(host="localhost",database="dss_pupuk", user="postgres", password="password")
	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	cur.execute("SELECT * FROM modelregresi")
	print "Total Rows: ", cur.rowcount
	#row = cur.fetchone()
 
	# while row is not None:
	#     print(row)
	#     row = cur.fetchone()

	rows = cur.fetchall()
	for row in rows:
		print row["nama_model"]
	cur.close()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if conn is not None:
        conn.close()


sentinel_file = "jonggol.tif"
shp_file = "kebun_jonggol_32478.shp"
clipped_file = "jonggol_clipped.tif"
format_file = "GTiff"

## ========== CLIP RASTER WITH SHAPEFILE  ====================
# warp_opts = gdal.WarpOptions(
#     format=format_file,
#     cutlineDSName=shp_file,
#     cropToCutline=True,
#     dstNodata=-9999,
#     xRes=10.0,
#     yRes=10.0,
# )
#gdal.Warp(clipped_file, filename, options=warp_opts,)

# gdalwarp -
# dstnodata -9999 
# -q 
# -cutline D:/Indra/Tesis/Ngoprek6/Basemap/kebun_jonggol_32478.shp 
# -crop_to_cutline 
# -tr 10.0 10.0 
# -of GTiff 
# D:/Indra/Tesis/Ngoprek6/Superres/Kebun_Jonggol_20170525_L2A.tif 
# D:/Indra/Tesis/Ngoprek6/Process/sample_clip.tif

## ==============  GET RASTER BANDS STATISTIC ==============
# g = gdal.Open(clipped_file)

# print "[ RASTER BAND COUNT ]: ", g.RasterCount

# for band in range( g.RasterCount ):
#     band += 1
#     print "[ GETTING BAND ]: ", band
#     srcband = g.GetRasterBand(band)
#     if srcband is None:
#         continue

#     stats = srcband.GetStatistics( True, True )
#     if stats is None:
#         continue

#     print "[ STATS ] =  Minimum=%.3f, Maximum=%.3f, Mean=%.3f, StdDev=%.3f" % ( \
#                 stats[0], stats[1], stats[2], stats[3] )



