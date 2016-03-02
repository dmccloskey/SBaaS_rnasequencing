from copy import copy
#sbaas
from .stage01_rnasequencing_genesFpkmTracking_query import stage01_rnasequencing_genesFpkmTracking_query
from .stage01_rnasequencing_analysis_query import stage01_rnasequencing_analysis_query
from .stage01_rnasequencing_heatmap_io import stage01_rnasequencing_heatmap_io
#sbaas models
from .stage01_rnasequencing_heatmap_postgresql_models import *
#resources
#from SBaaS_statistics.heatmap import fpkms_heatmap
from python_statistics.calculate_heatmap import calculate_heatmap

class stage01_rnasequencing_heatmap_execute(stage01_rnasequencing_heatmap_io,
                                            stage01_rnasequencing_genesFpkmTracking_query,
                                            stage01_rnasequencing_analysis_query):
    def execute_heatmap(self, analysis_id_I,gene_exclusion_list=[],
                row_pdist_metric_I='euclidean',row_linkage_method_I='complete',
                col_pdist_metric_I='euclidean',col_linkage_method_I='complete',
                order_sampleNameByGeneNameShort_I=False,
                sample_names_I=[],
                gene_name_shorts_I=[],):
        '''Execute hierarchical cluster on row and column data'''

        print('executing heatmap...');
        calculateheatmap =  calculate_heatmap();
        #fpkmsheatmap =  fpkms_heatmap();
        # get the analysis information
        experiment_ids,sample_names = [],[];
        experiment_ids,sample_names = self.get_experimentIDAndSampleName_analysisID_dataStage01RNASequencingAnalysis(analysis_id_I);
        fpkms_all = [];
        for sample_name_cnt,sample_name in enumerate(sample_names):
            # query fpkm data:
            fpkms = [];
            fpkms = self.get_rows_experimentIDAndSampleName_dataStage01RNASequencingGenesFpkmTracking(experiment_ids[sample_name_cnt],sample_name);
            fpkms_all.extend(fpkms);
        heatmap_O = [];
        dendrogram_col_O = [];
        dendrogram_row_O = [];
        if order_sampleNameByGeneNameShort_I:
            heatmap_1,dendrogram_col_1,dendrogram_row_1 = calculateheatmap.make_heatmap(fpkms_all,
                'sample_name','gene_short_name','FPKM',
                row_pdist_metric_I=row_pdist_metric_I,row_linkage_method_I=row_linkage_method_I,
                col_pdist_metric_I=col_pdist_metric_I,col_linkage_method_I=col_linkage_method_I,
                filter_rows_I=sample_names_I,
                filter_columns_I=gene_name_shorts_I,
                order_rowsFromTemplate_I=sample_names_I,
                order_columnsFromTemplate_I=gene_name_shorts_I,);
        else:
            heatmap_1,dendrogram_col_1,dendrogram_row_1 = calculateheatmap.make_heatmap(fpkms_all,
                'gene_short_name','sample_name','FPKM',
                row_pdist_metric_I=row_pdist_metric_I,row_linkage_method_I=row_linkage_method_I,
                col_pdist_metric_I=col_pdist_metric_I,col_linkage_method_I=col_linkage_method_I,
                filter_rows_I=gene_name_shorts_I,
                filter_columns_I=sample_names_I,
                order_rowsFromTemplate_I=gene_name_shorts_I,
                order_columnsFromTemplate_I=sample_names_I);
        # add data to to the database for the heatmap
        for d in heatmap_1:
            d['analysis_id']=analysis_id_I;
            d['value_units']='FPKM';
            d['used_']=True;
            d['comment_']=None;
            heatmap_O.append(d);
        ## add data to the database for the dendrograms
        dendrogram_col_1['analysis_id']=analysis_id_I;
        dendrogram_col_1['value_units']='FPKM';
        dendrogram_col_1['used_']=True;
        dendrogram_col_1['comment_']=None;
        dendrogram_col_O.append(dendrogram_col_1);
        dendrogram_row_1['analysis_id']=analysis_id_I;
        dendrogram_row_1['value_units']='FPKM';
        dendrogram_row_1['used_']=True;
        dendrogram_row_1['comment_']=None;
        dendrogram_row_O.append(dendrogram_row_1);
        self.add_rows_table('data_stage01_rnasequencing_heatmap',heatmap_O);
        #self.add_rows_table('data_stage01_rnasequencing',dendrogram_col_O);
        #self.add_rows_table('data_stage01_rnasequencing',dendrogram_row_O);