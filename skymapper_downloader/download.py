
import astropy, sys, logging

# configuration
TAP_URL = "http://api.skymapper.nci.org.au/public/tap"
TABLE_NAME = "dr1.dr1p1_master"
ID = "object_id"
TABLE_ROWS = "raj2000, dej2000, u_psf, e_u_psf, u_psf, e_v_psf, v_psf, e_g_psf, g_psf, e_r_psf, r_psf, e_r_psf, i_psf, e_i_psf, z_psf, e_z_psf"
MIN = 0
MAX = 31874195
BATCH_SIZE = 500000

logging.basicConfig(
    filename='download.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

# helper functions

def generate_filename(table, batch_min, batch_max):
        return f"{table}_{batch_min}-{batch_max}.fits"

def generate_command(url, query, filepath):
        return(f"timeout 3600 "
                f"java -jar stilts.jar "
                f"tapquery tapurl='{url}' "
                f"adql='{query}' "
                f"out='{filepath}'\n")

def show_details(table_name, id_name, the_min, the_max, batch_size):
        return (f"downloading {table_name} by {id_name}\n"
                f"from {float(the_min)/(10**6)}m to {float(the_max)/10**6}m\n"
                f"in batches of {float(batch_size)/10**6}m\n")