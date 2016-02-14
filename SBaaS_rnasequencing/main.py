import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings_1.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_rnasequencing')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/sequencing_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'sequencing_analysis')
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/calculate_utilities')

from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

'''make the analysis table'''
from SBaaS_rnasequencing.stage01_rnasequencing_analysis_execute import stage01_rnasequencing_analysis_execute
exanalysis01 = stage01_rnasequencing_analysis_execute(session,engine,pg_settings.datadir_settings);
exanalysis01.drop_dataStage01_rnasequencing_analysis();
exanalysis01.initialize_dataStage01_rnasequencing_analysis();
exanalysis01.reset_dataStage01_rnasequencing_analysis('ALEsKOs01_0_11_evo04pgi');
exanalysis01.import_dataStage01RNASequencingAnalysis_add('data/tests/analysis_rnasequencing/150806_RNASequencing_ALEsKOs01_analysis01.csv');

#'''analyze the genesFpkmTracking data'''
#from SBaaS_rnasequencing.stage01_rnasequencing_genesFpkmTracking_execute import stage01_rnasequencing_genesFpkmTracking_execute
#exfpkm01 = stage01_rnasequencing_genesFpkmTracking_execute(session,engine,pg_settings.datadir_settings);
#exfpkm01.drop_dataStage01_rnasequencing_genesFpkmTracking();
#exfpkm01.initialize_dataStage01_rnasequencing_genesFpkmTracking();

## reset the previous imports
#exfpkm01.reset_dataStage01_rnasequencing_genesFpkmTracking('ALEsKOs01');
## import the driver file
#iobase = base_importData();
#iobase.read_csv('data/tests/analysis_rnasequencing/150806_RNASequencing_ALEsKOs01_genesFpkmTracking01.csv');
#fileList = iobase.data;
## read in each data file
#for file in fileList:
#    print('importing genes.pfkm_tracking data for sample ' + file['sample_name']);
#    exfpkm01.import_dataStage01RNASequencingGenesFpkmTracking_add(file['filename'],file['experiment_id'],file['sample_name']);
#iobase.clear_data();

## export replicate boxAndWhiskers plot
#exfpkm01.export_dataStage01RNASequencingGenesFpkmTracking_js('ALEsKOs01_0_11_evo04pgi');

## make the heatmap
#from SBaaS_rnasequencing.stage01_rnasequencing_heatmap_execute import stage01_rnasequencing_heatmap_execute
#exheatmap01 = stage01_rnasequencing_heatmap_execute(session,engine,pg_settings.datadir_settings);
#exheatmap01.drop_dataStage01_rnasequencing_heatmap();
#exheatmap01.initialize_dataStage01_rnasequencing_heatmap();
#analysis_ids = [
#    'ALEsKOs01_0_11_evo04pgi'
#                ];
#for analysis in analysis_ids:
#    exheatmap01.reset_dataStage01_rnasequencing_heatmap(analysis);
#    exheatmap01.reset_dataStage01_rnasequencing_dendrogram(analysis);
#for analysis in analysis_ids:
#    exheatmap01.execute_heatmap(analysis);
## export the heatmap
#exheatmap01.export_dataStage01RNASequencingHeatmap_js('ALEsKOs01_0_11_evo04pgi');

#'''Analyse the gene expression differences'''
#from SBaaS_rnasequencing.stage01_rnasequencing_geneExpDiff_execute import stage01_rnasequencing_geneExpDiff_execute
#exged01 = stage01_rnasequencing_geneExpDiff_execute(session,engine,pg_settings.datadir_settings);
#exged01.drop_dataStage01_rnasequencing_geneExpDiff();
#exged01.initialize_dataStage01_rnasequencing_geneExpDiff();
## reset the previous imports
#exged01.reset_dataStage01_rnasequencing_geneExpDiff();
## import the driver file
#iobase = base_importData();
#iobase.read_csv('data/tests/analysis_rnasequencing/150806_RNASequencing_ALEsKOs01_geneExpDiff01.csv');
#fileList = iobase.data;
## read in each data file
#for file in fileList:
#    print('importing gene_exp.diff ' + file['filename']);
#    exged01.import_dataStage01RNASequencingGeneExpDiff_add(file['filename'],file['experiment_id_1'],file['experiment_id_2'],file['sample_name_abbreviation_1'],file['sample_name_abbreviation_2']);
#iobase.clear_data();

## export the volcano plot
#exged01.export_dataStage01RNASequencingGeneExpDiff_js('ALEsKOs01_0_11_evo04pgi');
