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
analysis_ids = [
        #expDiff and fpkmtracking ,
        'ALEsKOs01_RNASequencing_0_11_evo04Evo01',
        'ALEsKOs01_RNASequencing_0_11_evo04Evo02',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04gndEvo01',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04gndEvo02',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04gndEvo03',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo01',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo02',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo03',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo04',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo05',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo06',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo07',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo08',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04ptsHIcrrEvo01',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04ptsHIcrrEvo02',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04ptsHIcrrEvo03',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04ptsHIcrrEvo04',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04sdhCBEvo01',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04sdhCBEvo02',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04sdhCBEvo03',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04tpiAEvo01',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04tpiAEvo02',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04tpiAEvo03',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04tpiAEvo04',       
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04gnd',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgi',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04ptsHIcrr',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04sdhCB',
        'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04tpiA',
        'ALEsKOs01_RNASequencing_0_11_evo04', ];
for analysis_id in analysis_ids:
    analysis_id_geneExp = analysis_id.replace('RNASequencing_','');
    genes = ged01.get_genes_analysisIDAndFCAndQValue_dataStage01RNASequencingGeneExpDiff(
            analysis_id_I=analysis_id_geneExp,
            fold_change_log2_threshold_I = 2,
            q_value_threshold_I = 0.05);
    if not genes:
        print(analysis_id);


#make the table
from SBaaS_rnasequencing.stage01_rnasequencing_genesCountTable_execute import stage01_rnasequencing_genesCountTable_execute
gct01 = stage01_rnasequencing_genesCountTable_execute(session,engine,pg_settings.datadir_settings);
gct01.initialize_supportedTables();
gct01.drop_tables();
gct01.initialize_tables();

#from io_utilities.base_importData import base_importData
#from io_utilities.base_exportData import base_exportData

## import the driver file
#iobase = base_importData();
#iobase.read_csv(pg_settings.datadir_settings['workspace_data']+'/_input/160712_RNASequencing_dataStage01GeneCountTable01.csv');
#fileList = iobase.data;
## read in each data file
#for file in fileList:
#   print('importing genes.count/fpkm/attr_able for analysis ' + file['analysis_id']);
#   gct01.import_dataStage01RNASequencingGenesCountTable_add(
#       file['genes_count_table_dir'],
#       file['genes_fpkm_table_dir'],
#       file['genes_attr_table_dir'],
#       file['analysis_id'],
#       file['experiment_ids'],
#       file['samples_host_dirs'],
#       file['samples_names']);
#iobase.clear_data();