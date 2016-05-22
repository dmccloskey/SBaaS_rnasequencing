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

#fpkm01.export_dataStage01RNASequencingGenesFpkmTracking_pairWisePlot_js('ALEsKOs01_0_evo04_11_evo04Evo01');

#make the table
from SBaaS_rnasequencing.stage01_rnasequencing_geneExpDiff_execute import stage01_rnasequencing_geneExpDiff_execute
ged01 = stage01_rnasequencing_geneExpDiff_execute(session,engine,pg_settings.datadir_settings);
ged01.initialize_supportedTables();
ged01.initialize_tables();

#ged01.export_dataStage01RNASequencingGeneExpDiff_count_js();
ged01.export_dataStage01RNASequencingGeneExpDiffFpkmTracking_js(
    analysis_ids_I=['ALEsKOs01_0_evo04_0_evo04tpiA',
                    'ALEsKOs01_0_evo04_11_evo04tpiAEvo01',
                    'ALEsKOs01_0_evo04_11_evo04tpiAEvo02',
                    'ALEsKOs01_0_evo04_11_evo04tpiAEvo03',
                    'ALEsKOs01_0_evo04_11_evo04tpiAEvo04',
                    'ALEsKOs01_0_11_evo04tpiAEvo01',
                    'ALEsKOs01_0_11_evo04tpiAEvo02',
                    'ALEsKOs01_0_11_evo04tpiAEvo03',
                    'ALEsKOs01_0_11_evo04tpiAEvo04',],
    gene_short_names_I=['aceE','aceF','lpd']
    )
#ged01.export_dataStage01RNASequencingGeneExpDiffFpkmTracking_js(
#    analysis_ids_I=['ALEsKOs01_0_evo04_0_evo04ptsHIcrr',
#                    'ALEsKOs01_0_evo04_11_evo04ptsHIcrrEvo01',
#                    'ALEsKOs01_0_evo04_11_evo04ptsHIcrrEvo02',
#                    'ALEsKOs01_0_evo04_11_evo04ptsHIcrrEvo03',
#                    'ALEsKOs01_0_evo04_11_evo04ptsHIcrrEvo04',],
#    gene_short_names_I=['lexA','recA','umuC','umuD','rulA']
#    )