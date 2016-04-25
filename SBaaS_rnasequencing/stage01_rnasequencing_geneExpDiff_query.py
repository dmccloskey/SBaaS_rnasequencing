#sbaas
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query
#sbaas models
from .stage01_rnasequencing_geneExpDiff_postgresql_models import *

class stage01_rnasequencing_geneExpDiff_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_rnasequencing_geneExpDiff':data_stage01_rnasequencing_geneExpDiff,
                            'data_stage01_rnasequencing_geneExpDiffFpkmTracking':data_stage01_rnasequencing_geneExpDiffFpkmTracking,
                        };
        self.set_supportedTables(tables_supported);
    # query data from data_stage01_rnasequencing_geneExpDiff
    def get_rows_experimentIDsAndSampleNameAbbreviations_dataStage01RNASequencingGeneExpDiff(self,experiment_id_1_I,experiment_id_2_I,sample_name_abbreviation_1_I,sample_name_abbreviation_2_I):
        '''Query rows by experiment_ids 1 and 2 and sample_name_abbreviations 1 and 2'''
        try:
            data = self.session.query(data_stage01_rnasequencing_geneExpDiff).filter(
                    data_stage01_rnasequencing_geneExpDiff.experiment_id_1.like(experiment_id_1_I),
                    data_stage01_rnasequencing_geneExpDiff.experiment_id_2.like(experiment_id_2_I),
                    data_stage01_rnasequencing_geneExpDiff.sample_name_abbreviation_1.like(sample_name_abbreviation_1_I),
                    data_stage01_rnasequencing_geneExpDiff.sample_name_abbreviation_2.like(sample_name_abbreviation_2_I),
                    data_stage01_rnasequencing_geneExpDiff.used_).all();
            data_O = [];
            for d in data: 
                data_dict = {'id':d.id,
                #'analysis_id':d.analysis_id,
                'experiment_id_1':d.experiment_id_1,
                'experiment_id_2':d.experiment_id_2,
                'sample_name_abbreviation_1':d.sample_name_abbreviation_1,
                'sample_name_abbreviation_2':d.sample_name_abbreviation_2,
                'test_id':d.test_id,
                'gene_id':d.gene_id,
                'gene':d.gene,
                'sample_1':d.sample_1,
                'sample_2':d.sample_2,
                'status':d.status,
                'value_1':d.value_1,
                'value_2':d.value_2,
                'fold_change_log2':d.fold_change_log2,
                'test_stat':d.test_stat,
                'p_value':d.p_value,
                'q_value':d.q_value,
                'significant':d.significant,
                'used_':d.used_,
                'comment_':d.comment_};
                data_O.append(data_dict);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def add_dataStage01RNASequencingGeneExpDiff(self, data_I):
        '''add rows of data_stage01_rnasequencing_geneExpDiff'''
        if data_I:
            for d in data_I:
                try:
                    if not 'fold_change_log2' in d and 'log2(fold_change)' in d:
                        d['fold_change_log2'] = d['log2(fold_change)'];
                    if not 'used_' in d:
                        d['used_'] = True;
                    if not 'comment_' in d:
                        d['comment_'] = None;
                    data_add = data_stage01_rnasequencing_geneExpDiff(d
                            #d['experiment_id_1'],
                            #d['experiment_id_2'],
                            #d['sample_name_abbreviation_1'],
                            #d['sample_name_abbreviation_2'],
                            #d['test_id'],
                            #d['gene_id'],
                            #d['gene'],
                            #d['sample_1'],
                            #d['sample_2'],
                            #d['status'],
                            #d['value_1'],
                            #d['value_2'],
                            #d['log2(fold_change)'],
                            #d['test_stat'],
                            #d['p_value'],
                            #d['q_value'],
                            #d['significant'],
                            #d['used_'],
                            #d['comment_']
                            );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01RNASequencingGeneExpDiff(self,data_I):
        '''update rows of data_stage01_rnasequencing_lineage'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_rnasequencing_geneExpDiff).filter(
                           data_stage01_rnasequencing_geneExpDiff.id==d['id']).update(
                            {'experiment_id_1':d['experiment_id_1'],
                            'experiment_id_2':d['experiment_id_2'],
                            'sample_name_abbreviation_1':d['sample_name_abbreviation_1'],
                            'sample_name_abbreviation_2':d['sample_name_abbreviation_2'],
                            'test_id':d['test_id'],
                            'gene_id':d['gene_id'],
                            'gene':d['gene'],
                            'sample_1':d['sample_1'],
                            'sample_2':d['sample_2'],
                            'status':d['status'],
                            'value_1':d['value_1'],
                            'value_2':d['value_2'],
                            'fold_change_log2':d['fold_change_log2'],
                            'test_stat':d['test_stat'],
                            'p_value':d['p_value'],
                            'q_value':d['q_value'],
                            'significant':d['significant'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def getAggregateFunction_rows_dataStage01RNASequencingGeneExpDiff(self,
                column_name_I = 'gene',
                aggregate_function_I='count',
                aggregate_label_I='count_1',
                query_I={},
                output_O='scalar',
                dictColumn_I=None):
        '''Query row count by analysis_id from data_stage01_rnasequencing_geneExpDiff
        INPUT:
        analysis_id_I = string
        column_name_I = string
        aggregate_function_I = name of the aggregate function to call on the column
        output_O = string
        dictColumn_I = string
        OPTIONAL INPUT:
        query_I = additional query blocks
        OUTPUT:
        data_O = output specified by output_O and dictColumn_I
        '''

        tables = ['data_stage01_rnasequencing_geneExpDiff'];
        # get the listDict data
        data_O = [];
        query = {};
        query['select'] = [
            {"table_name":tables[0],
             "column_name":column_name_I,
             'aggregate_function':aggregate_function_I,
             'label':aggregate_label_I,
             }
            ];
        query['where'] = [
            {"table_name":tables[0],
            'column_name':'used_',
            'value':'true',
            'operator':'IS',
            'connector':'AND'
                },
	    ];

        #additional query blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;

    # query data from data_stage01_rnasequencing_geneExpDiffFpkmTracking
    def get_rows_analysisID_dataStage01RNASequencingGeneExpDiffFpkmTracking(self,analysis_id_I):
        '''Query rows by analysis_id'''
        try:
            data = self.session.query(data_stage01_rnasequencing_geneExpDiffFpkmTracking).filter(
                    data_stage01_rnasequencing_geneExpDiffFpkmTracking.analysis_id.like(analysis_id_I),
                    data_stage01_rnasequencing_geneExpDiffFpkmTracking.used_).all();
            data_O = [d.__repr__dict__() for d in data];
            return data_O;
        except SQLAlchemyError as e:
            print(e);