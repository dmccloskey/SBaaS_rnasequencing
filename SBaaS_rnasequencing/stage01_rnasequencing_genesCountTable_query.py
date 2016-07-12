#sbaas
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query
#sbaas models
from .stage01_rnasequencing_genesCountTable_postgresql_models import *

class stage01_rnasequencing_genesCountTable_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_rnasequencing_genesCountTable':data_stage01_rnasequencing_genesCountTable,
                        };
        self.set_supportedTables(tables_supported);
    # query data from data_stage01_rnasequencing_genesCountTable
    def get_rows_experimentIDAndSampleName_dataStage01RNASequencingGenesCountTable(self,experiment_id_I,sample_name_I):
        '''Query rows by experiment_id and sample_name'''
        try:
            data = self.session.query(data_stage01_rnasequencing_genesCountTable).filter(
                    data_stage01_rnasequencing_genesCountTable.experiment_id.like(experiment_id_I),
                    data_stage01_rnasequencing_genesCountTable.sample_name.like(sample_name_I),
                    data_stage01_rnasequencing_genesCountTable.used_).all();
            data_O = [d.__repr__dict__() for d in data];
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_analysisID_dataStage01RNASequencingGenesCountTable(self,analysis_id_I,):
        '''Query rows by analysis_id'''
        try:
            data = self.session.query(data_stage01_rnasequencing_genesCountTable).filter(
                    data_stage01_rnasequencing_genesCountTable.analysis_id.like(analysis_id_I),
                    data_stage01_rnasequencing_genesCountTable.used_).all();
            data_O = [d.__repr__dict__() for d in data];
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def add_dataStage01RNASequencingGenesCountTable(self, data_I):
        '''add rows of data_stage01_rnasequencing_fpkmTable'''
        if data_I:
            for d in data_I:
                try:
                    if not 'used_' in d:
                        d['used_'] = True;
                    if not 'comment_' in d:
                        d['comment_'] = None;
                    data_add = data_stage01_rnasequencing_genesCountTable(d
                            );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();