#system
import json
from math import log
#sbaas
from .stage01_rnasequencing_geneExpDiff_query import stage01_rnasequencing_geneExpDiff_query
from .stage01_rnasequencing_analysis_query import stage01_rnasequencing_analysis_query
from SBaaS_base.sbaas_template_io import sbaas_template_io

# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from sequencing_analysis.gene_exp_diff import gene_exp_diff
from ddt_python.ddt_container import ddt_container
from ddt_python.ddt_container_filterMenuAndChart2dAndTable import ddt_container_filterMenuAndChart2dAndTable
from listDict.listDict import listDict

class stage01_rnasequencing_geneExpDiff_io(stage01_rnasequencing_geneExpDiff_query,
                                           stage01_rnasequencing_analysis_query,
                                           sbaas_template_io):

    def import_dataStage01RNASequencingGeneExpDiff_add(self, filename,experiment_id_1,experiment_id_2,sample_name_abbreviation_1,sample_name_abbreviation_2):
        '''table adds'''
        geneexpdiff = gene_exp_diff();
        geneexpdiff.import_geneExpDiff(filename_I=filename,experiment_id_1_I = experiment_id_1,experiment_id_2_I = experiment_id_2,
                        sample_name_abbreviation_1_I = sample_name_abbreviation_1,sample_name_abbreviation_2_I = sample_name_abbreviation_2);
        self.add_dataStage01RNASequencingGeneExpDiff(geneexpdiff.geneExpDiff);

    def import_dataStage01RNASequencingGeneExpDiffFpkmTracking_add(self, filename,analysis_id,experiment_id_1,experiment_id_2,sample_name_abbreviation_1,sample_name_abbreviation_2):
        '''table adds'''
        geneexpdiff = gene_exp_diff();
        geneexpdiff.import_genesFpkmTracking(filename_I=filename,analysis_id_I=analysis_id, experiment_id_1_I = experiment_id_1,experiment_id_2_I = experiment_id_2,
                        sample_name_abbreviation_1_I = sample_name_abbreviation_1,sample_name_abbreviation_2_I = sample_name_abbreviation_2);
        self.add_rows_table('data_stage01_rnasequencing_geneExpDiffFpkmTracking',geneexpdiff.genesFpkmTracking);

    def import_dataStage01RNASequencingGeneExpDiff_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01RNASequencingGeneExpDiff(data.data);
        data.clear_data();
        
    def export_dataStage01RNASequencingGeneExpDiff_js(self,analysis_id_I,p_value_I=0.01,fold_change_log2_I=1.0,data_dir_I='tmp'):
        '''Export data differentially expressed genes as a Volcano Plot
        INPUT:
        OUTPUT:
        '''
        
        # get the analysis information
        experiment_ids,sample_name_abbreviations = [],[];
        experiment_ids,sample_name_abbreviations = self.get_experimentIDAndSampleNameAbbreviation_analysisID_dataStage01RNASequencingAnalysis(analysis_id_I);
        data_O = [];
        for sample_name_abbreviation_cnt_1,sample_name_abbreviation_1 in enumerate(sample_name_abbreviations):
            for sample_name_abbreviation_cnt_2,sample_name_abbreviation_2 in enumerate(sample_name_abbreviations):
                if sample_name_abbreviation_cnt_1 != sample_name_abbreviation_cnt_2:
                    # query geneExpDiff data:
                    geneExpDiff_tmp = [];
                    geneExpDiff_tmp = self.get_rows_experimentIDsAndSampleNameAbbreviations_dataStage01RNASequencingGeneExpDiff(experiment_ids[sample_name_abbreviation_cnt_1],experiment_ids[sample_name_abbreviation_cnt_2],sample_name_abbreviation_1,sample_name_abbreviation_2);
                    geneExpDiff = [];
                    for d in geneExpDiff_tmp:
                        if not 'p_value_negLog10' in d:
                            d['p_value_negLog10']=-log(d['p_value'],10.0);
                        if p_value_I and fold_change_log2_I and d['p_value'] and d['fold_change_log2'] and d['p_value']<=p_value_I and (d['fold_change_log2']>=fold_change_log2_I or d['fold_change_log2']<=-fold_change_log2_I):
                            geneExpDiff.append(d);
                        elif not p_value_I and not fold_change_log2_I and d['p_value'] and d['fold_change_log2']:
                            geneExpDiff.append(d);
                    data_O.extend(geneExpDiff);
        # make the data parameters
        data1_keys = ['experiment_id_1','experiment_id_2','sample_name_abbreviation_1','sample_name_abbreviation_2','gene','fold_change_log2','p_value_negLog10','significant'
                    ];
        data1_nestkeys = ['experiment_id_1'];
        data1_keymap = {'ydata':'p_value_negLog10',
                        'xdata':'fold_change_log2',
                        'serieslabel':'',
                        'featureslabel':'gene'};
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'volcanoplot2d_01',"svgkeymap":[data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 50, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":'Fold Change [log2(FC)]',"svgy1axislabel":'Probability [-log10(P)]',
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_O = {'tileheader':'Volcano plot','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        svgtileparameters_O.update(svgparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'pairWiseTest','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0],"tile3":[0]};
        # dump the data to a json file
        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = None);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects());
    def export_dataStage01RNASequencingGeneExpDiff_count_js(self,
                query_I={'where':[
                    {"table_name":'data_stage01_rnasequencing_geneExpDiff',
                    'column_name':'experiment_id_1',
                    'value':'ALEsKOs01',
                    'operator':'LIKE',
                    'connector':'AND'
                        },
                    ],
                },
                data_dir_I='tmp'):
        '''Export data for a count of differentially expressed genes
        '''
        
        # get the analysis information
        query = {}
        tables = ['data_stage01_rnasequencing_geneExpDiff'];
        query['select'] = [
            {"table_name":tables[0],
             "column_name":'experiment_id_1',
             },{"table_name":tables[0],
             "column_name":'experiment_id_2',
             },{"table_name":tables[0],
             "column_name":'sample_name_abbreviation_1',
             },{"table_name":tables[0],
             "column_name":'sample_name_abbreviation_2',
             },
            ];
        query['group_by'] = [
            {"table_name":tables[0],
             "column_name":'experiment_id_1',
             },{"table_name":tables[0],
             "column_name":'experiment_id_2',
             },{"table_name":tables[0],
             "column_name":'sample_name_abbreviation_1',
             },{"table_name":tables[0],
             "column_name":'sample_name_abbreviation_2',
             },
            ];
        query['order_by'] = [
            {"table_name":tables[0],
             "column_name":'experiment_id_1',
             "order":'ASC',
             },{"table_name":tables[0],
             "column_name":'experiment_id_2',
             "order":'ASC',
             },{"table_name":tables[0],
             "column_name":'sample_name_abbreviation_1',
             "order":'ASC',
             },{"table_name":tables[0],
             "column_name":'sample_name_abbreviation_2',
             "order":'ASC',
             },
            ];
        query['where'] = [
            {"table_name":tables[0],
            'column_name':'significant',
            'value':'yes',
            'operator':'LIKE',
            'connector':'AND'
                },
            ];

        #additional query blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);

        data_O = [];
        data_O = self.getAggregateFunction_rows_dataStage01RNASequencingGeneExpDiff(
                column_name_I = 'gene',
                aggregate_function_I='count',
                aggregate_label_I='count_1',
                query_I=query,
                output_O='listDict',
                dictColumn_I=None);
        # add in new column
        for d in data_O:
            d['condition'] = ('%s_%s'%(d['sample_name_abbreviation_1'],d['sample_name_abbreviation_2']))
        # make the data parameters
        data1_keys = list(data_O[0].keys());
        data1_nestkeys = ['sample_name_abbreviation_1'];
        data1_keymap = {'ydata':'count_1',
                        'xdata':'condition',
                        'serieslabel':'sample_name_abbreviation_2',
                        'featureslabel':'condition',
                        'tooltiplabel':'condition'};
        # make the data object
        

        nsvgtable = ddt_container_filterMenuAndChart2dAndTable();
        nsvgtable.make_filterMenuAndChart2dAndTable(
                data_filtermenu=data_O,
                data_filtermenu_keys=data1_keys,
                data_filtermenu_nestkeys=data1_nestkeys,
                data_filtermenu_keymap=data1_keymap,
                data_svg_keys=None,
                data_svg_nestkeys=None,
                data_svg_keymap=None,
                data_table_keys=None,
                data_table_nestkeys=None,
                data_table_keymap=None,
                data_svg=None,
                data_table=None,
                svgtype='verticalbarschart2d_01',
                tabletype='responsivetable_01',
                svgx1axislabel='Condition',
                svgy1axislabel='Count',
                tablekeymap = [data1_keymap],
                svgkeymap = [data1_keymap],
                formtile2datamap=[0],
                tabletile2datamap=[0],
                svgtile2datamap=[0],
                svgfilters=None,
                svgtileheader='Significant DE count',
                tablefilters=None,
                tableheaders=None
                );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());
    def export_dataStage01RNASequencingGeneExpDiffFpkmTracking_js(
        self,analysis_ids_I,gene_short_names_I=[],query_I={},data_dir_I='tmp'):
        '''Export data as a bullet chart
        INPUT:
        OUTPUT:
        '''
        
        data_O = [];
        # get fpkm tracking data
        data_O = self.get_rows_analysisIDAndGeneShortNames_dataStage01RNASequencingGeneExpDiffFpkmTracking(
            analysis_ids_I,
            gene_short_names_I,
            query_I=query_I,
            output_O='listDict',
            dictColumn_I=None);

        # make the data parameters
        data1_keys = [
            'analysis_id',
            'experiment_id',
            'sample_name_abbreviation',
            #'gene_id',
            'gene_short_name',
                    ];
        data1_nestkeys = ['gene_short_name'];
        data1_keymap = {
                'ydata':'FPKM',
                'ydatamean':'FPKM',
                'ydatalb':'FPKM_conf_lo',
                'ydataub':'FPKM_conf_hi',
                'xdata':'gene_short_name',
                'serieslabel':'sample_name_abbreviation',
                'featureslabel':'sample_name_abbreviation',
                'tooltiplabel':'gene_short_name'};
        
        nsvgtable = ddt_container_filterMenuAndChart2dAndTable();
        nsvgtable.make_filterMenuAndChart2dAndTable(
                data_filtermenu=data_O,
                data_filtermenu_keys=data1_keys,
                data_filtermenu_nestkeys=data1_nestkeys,
                data_filtermenu_keymap=data1_keymap,
                data_svg_keys=None,
                data_svg_nestkeys=None,
                data_svg_keymap=None,
                data_table_keys=None,
                data_table_nestkeys=None,
                data_table_keymap=None,
                data_svg=None,
                data_table=None,
                svgtype='boxandwhiskersplot2d_01',
                tabletype='responsivetable_01',
                svgx1axislabel='',
                svgy1axislabel='FPKM',
                tablekeymap = [data1_keymap],
                svgkeymap = [data1_keymap],
                formtile2datamap=[0],
                tabletile2datamap=[0],
                svgtile2datamap=[0],
                svgfilters=None,
                svgtileheader='Cuffdiff FPKM',
                tablefilters=None,
                tableheaders=None,
                svgparameters_I={"svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                                "svgwidth":500,"svgheight":350,}
                );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());