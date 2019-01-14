# Test Databrary functions

import dbpy

print("Starting tests.")
dbpy.assign_constants()
dbpy.get_db_stats()
dbpy.login_db("rogilmore@psu.edu")
dbpy.is_institution()
dbpy.is_person()
dbpy.get_asset_segment_range()
dbpy.get_institution()
dbpy.get_person()
dbpy.download_party()
dbpy.download_session_csv()
dbpy.get_supported_file_types()
dbpy.list_sessions_in_volume()
dbpy.download_containers_records()
print("Tests complete.")
