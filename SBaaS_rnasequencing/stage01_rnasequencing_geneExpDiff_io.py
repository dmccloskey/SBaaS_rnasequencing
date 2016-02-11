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

class stage01_rnasequencing_geneExpDiff_io(stage01_rnasequencing_geneExpDiff_query,
                                           stage01_rnasequencing_analysis_query,
                                           sbaas_template_io):

    def import_dataStage01RNASequencingGeneExpDiff_add(self, filename,experiment_id_1,experiment_id_2,sample_name_abbreviation_1,sample_name_abbreviation_2):
        '''table adds'''
        geneexpdiff = gene_exp_diff();
        geneexpdiff.import_geneExpDiff(filename_I=filename,experiment_id_1_I = experiment_id_1,experiment_id_2_I = experiment_id_2,
                        sample_name_abbreviation_1_I = sample_name_abbreviation_1,sample_name_abbreviation_2_I = sample_name_abbreviation_2);
        self.add_dataStage01RNASequencingGeneExpDiff(geneexpdiff.geneExpDiff);

    def import_dataStage01RNASequencingGeneExpDiff_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01RNASequencingGeneExpDiff(data.data);
        data.clear_data();
        
    def export_dataStage01RNASequencingGeneExpDiff_js(self,analysis_id_I,p_value_I=0.01,fold_change_log2_I=1.0,data_dir_I='tmp'):
        '''Export data for a volcano plot'''
        
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
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = self.settings['visualization_data'] + '/project/' + analysis_id_I + '_data_stage01_rnasequencing_heatmap' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);