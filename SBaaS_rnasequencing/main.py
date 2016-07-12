'''
TODO:
table for .fastq file locations
table for bowtie parameters
table for .bam/.sam files
table for cufflink parameters
table for cuffdiff parameters
'''


import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
# SBaaS paths:
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_base')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_rnasequencing')
# SBaaS dependencies paths:
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/python_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/r_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/listDict')
sys.path.append(pg_settings.datadir_settings['github']+'/ddt_python')
sys.path.append(pg_settings.datadir_settings['github']+'/sequencing_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/sequencing_analysis')

#make the genesFpkmTracking table'
from SBaaS_rnasequencing.stage01_rnasequencing_genesFpkmTracking_execute import stage01_rnasequencing_genesFpkmTracking_execute
fpkm01 = stage01_rnasequencing_genesFpkmTracking_execute(session,engine,pg_settings.datadir_settings);
fpkm01.initialize_supportedTables();
fpkm01.initialize_dataStage01_rnasequencing_genesFpkmTracking();

#make the table
from SBaaS_rnasequencing.stage01_rnasequencing_geneExpDiff_execute import stage01_rnasequencing_geneExpDiff_execute
ged01 = stage01_rnasequencing_geneExpDiff_execute(session,engine,pg_settings.datadir_settings);
ged01.initialize_supportedTables();
ged01.initialize_tables();

#make the table
from SBaaS_rnasequencing.stage01_rnasequencing_genesCountTable_execute import stage01_rnasequencing_genesCountTable_execute
gct01 = stage01_rnasequencing_genesCountTable_execute(session,engine,pg_settings.datadir_settings);
gct01.initialize_supportedTables();
gct01.drop_tables();
gct01.initialize_tables();

from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

# import the driver file
iobase = base_importData();
iobase.read_csv(pg_settings.datadir_settings['workspace_data']+'/_input/160712_RNASequencing_dataStage01GeneCountTable01.csv');
fileList = iobase.data;
# read in each data file
for file in fileList:
   print('importing genes.count/fpkm/attr_able for analysis ' + file['analysis_id']);
   gct01.import_dataStage01RNASequencingGenesCountTable_add(
       file['genes_count_table_dir'],
       file['genes_fpkm_table_dir'],
       file['genes_attr_table_dir'],
       file['analysis_id'],
       file['experiment_ids'],
       file['samples_host_dirs'],
       file['samples_names']);
iobase.clear_data();