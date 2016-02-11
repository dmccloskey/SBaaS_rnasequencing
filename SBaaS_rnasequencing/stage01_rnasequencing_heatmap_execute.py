from copy import copy
#sbaas
from .stage01_rnasequencing_genesFpkmTracking_query import stage01_rnasequencing_genesFpkmTracking_query
from .stage01_rnasequencing_analysis_query import stage01_rnasequencing_analysis_query
from .stage01_rnasequencing_heatmap_io import stage01_rnasequencing_heatmap_io
#sbaas models
from .stage01_rnasequencing_heatmap_postgresql_models import *
#resources
#from SBaaS_statistics.heatmap import fpkms_heatmap
from calculate_utilities.calculate_heatmap import calculate_heatmap

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
        mutationsheatmap =  mutations_heatmap();
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
        dendrogram_col_O = {};
        dendrogram_row_O = {};
        if order_sampleNameByGeneNameShort_I:
            heatmap_O,dendrogram_col_O,dendrogram_row_O = calculateheatmap.make_heatmap(fpkms_all,
                'sample_name','gene_short_name','FPKM',
                row_pdist_metric_I=row_pdist_metric_I,row_linkage_method_I=row_linkage_method_I,
                col_pdist_metric_I=col_pdist_metric_I,col_linkage_method_I=col_linkage_method_I,
                filter_rows_I=sample_names_I,
                filter_columns_I=gene_name_shorts_I,
                order_rowsFromTemplate_I=sample_names_I,
                order_columnsFromTemplate_I=gene_name_shorts_I,);
        else:
            heatmap_O,dendrogram_col_O,dendrogram_row_O = calculateheatmap.make_heatmap(fpkms_all,
                'gene_short_name','sample_name','FPKM',
                row_pdist_metric_I=row_pdist_metric_I,row_linkage_method_I=row_linkage_method_I,
                col_pdist_metric_I=col_pdist_metric_I,col_linkage_method_I=col_linkage_method_I,
                filter_rows_I=gene_name_shorts_I,
                filter_columns_I=sample_names_I,
                order_rowsFromTemplate_I=gene_name_shorts_I,
                order_columnsFromTemplate_I=sample_names_I);
        #fpkmsheatmap.genesFpkmTracking = fpkms_all;
        #fpkmsheatmap.sample_names = sample_names;
        #fpkmsheatmap.make_heatmap(gene_exclusion_list=gene_exclusion_list,
        #        row_pdist_metric_I=row_pdist_metric_I,row_linkage_method_I=row_linkage_method_I,
        #        col_pdist_metric_I=col_pdist_metric_I,col_linkage_method_I=col_linkage_method_I)
        #heatmap_O = fpkmsheatmap.heatmap;
        #dendrogram_col_O = fpkmsheatmap.dendrogram_col;
        #dendrogram_row_O = fpkmsheatmap.dendrogram_row;
        # add data to to the database for the heatmap
        for d in heatmap_O:
            row = None;
            row = data_stage01_rnasequencing_heatmap(
                analysis_id_I,
                d['col_index'],
                d['row_index'],
                d['value'],
                d['col_leaves'],
                d['row_leaves'],
                d['col_label'],
                d['row_label'],
                d['col_pdist_metric'],
                d['row_pdist_metric'],
                d['col_linkage_method'],
                d['row_linkage_method'],
                'fpkm',True, None);
            self.session.add(row);
        ## add data to the database for the dendrograms
        #row = None;
        #row = data_stage01_rnasequencing_dendrogram(
        #    analysis_id_I,
        #    dendrogram_col_O['leaves'],
        #    dendrogram_col_O['icoord'],
        #    dendrogram_col_O['dcoord'],
        #    dendrogram_col_O['ivl'],
        #    dendrogram_col_O['colors'],
        #    dendrogram_col_O['pdist_metric'],
        #    dendrogram_col_O['pdist_metric'],
        #    'fpkm',True, None);
        #self.session.add(row);
        #row = None;
        #row = data_stage01_rnasequencing_dendrogram(
        #    analysis_id_I,
        #    dendrogram_row_O['leaves'],
        #    dendrogram_row_O['icoord'],
        #    dendrogram_row_O['dcoord'],
        #    dendrogram_row_O['ivl'],
        #    dendrogram_row_O['colors'],
        #    dendrogram_row_O['pdist_metric'],
        #    dendrogram_row_O['pdist_metric'],
        #    'fpkm',True, None);
        #self.session.add(row);
        self.session.commit();