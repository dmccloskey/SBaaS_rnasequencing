#system
import json
#sbaas
from .stage01_rnasequencing_genesFpkmTracking_query import stage01_rnasequencing_genesFpkmTracking_query
from .stage01_rnasequencing_analysis_query import stage01_rnasequencing_analysis_query
from SBaaS_base.sbaas_template_io import sbaas_template_io

# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from sequencing_analysis.genes_fpkm_tracking import genes_fpkm_tracking
from ddt_python.ddt_container_filterMenuAndChart2dAndTable import ddt_container_filterMenuAndChart2dAndTable
from listDict.listDict import listDict

class stage01_rnasequencing_genesFpkmTracking_io(stage01_rnasequencing_genesFpkmTracking_query,
                                                 stage01_rnasequencing_analysis_query,
                                           sbaas_template_io):

    def import_dataStage01RNASequencingGenesFpkmTracking_add(self,filename,experiment_id,sample_name):
        '''table adds'''
        genesfpkmtracking = genes_fpkm_tracking();
        genesfpkmtracking.import_genesFpkmTracking(filename_I=filename,experiment_id_I = experiment_id,sample_name_I = sample_name);
        self.add_dataStage01RNASequencingGenesFpkmTracking(genesfpkmtracking.genesFpkmTracking);

    def import_dataStage01RNASequencingGenesFpkmTracking_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01RNASequencingGenesFpkmTracking(data.data);
        data.clear_data();
    def export_dataStage01RNASequencingGenesFpkmTracking_js(self,analysis_id_I,data_dir_I='tmp'):
        '''Export data for a box and whiskers plot'''
        # get the analysis information
        experiment_ids,sample_names = [],[];
        experiment_ids,sample_names = self.get_experimentIDAndSampleName_analysisID_dataStage01RNASequencingAnalysis(analysis_id_I);
        data_O = [];
        for sample_name_cnt,sample_name in enumerate(sample_names):
            # query fpkm data:
            fpkms = [];
            fpkms = self.get_rows_experimentIDAndSampleName_dataStage01RNASequencingGenesFpkmTracking(experiment_ids[sample_name_cnt],sample_name);
            data_O.extend(fpkms);
        # dump chart parameters to a js files
        data1_keys = ['experiment_id','sample_name','gene_short_name'
                    ];
        data1_nestkeys = ['gene_short_name'];
        data1_keymap = {'xdata':'gene_short_name',
                        'ydatamean':'FPKM',
                        'ydatalb':'FPKM_conf_lo',
                        'ydataub':'FPKM_conf_hi',
                        'serieslabel':'sample_name',
                        'featureslabel':'gene_short_name'};
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'boxandwhiskersplot2d_01',"svgkeymap":[data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":"gene","svgy1axislabel":"FPKM",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_O = {'tileheader':'Custom box and whiskers plot','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        svgtileparameters_O.update(svgparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'FPKM','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0],"tile3":[0]};
        # dump the data to a json file
        # dump the data to a json file
        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = None);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects());
    def export_dataStage01RNASequencingGenesFpkmTracking_pairWisePlot_js(self,analysis_id_I,data_dir_I='tmp'):
        '''Export data for a pairwise scatter plot
        INPUT:
        analysis_id
        data_dir_I
        OUTPUT:
        '''
        # get the analysis information
        experiment_ids,sample_names = [],[];
        experiment_ids,sample_names = self.get_experimentIDAndSampleName_analysisID_dataStage01RNASequencingAnalysis(analysis_id_I);
        data_O = [];
        for sample_name_cnt,sample_name in enumerate(sample_names):
            # query fpkm data:
            fpkms = [];
            fpkms = self.get_rows_experimentIDAndSampleName_dataStage01RNASequencingGenesFpkmTracking(experiment_ids[sample_name_cnt],sample_name);
            data_O.extend(fpkms);
        # reorganize the data
        listdict = listDict(data_O);
        data_O,columnValueHeader_O = listdict.convert_listDict2ColumnGroupListDict(
                    value_labels_I = ['FPKM','FPKM_conf_lo','FPKM_conf_hi'],
                    column_label_I = 'sample_name',
                    feature_labels_I = ['experiment_id','gene_id','gene_short_name'],
                    na_str_I=0.0,
                    columnValueConnector_str_I='_-_',
                    );
        # make the tile object
        #data1 = filtermenu/table
        data1_keymap_table = {
            'xdata':'svd_method',
            'ydata':'singular_value_index',
            'zdata':'d_vector',
            'rowslabel':'svd_method',
            'columnslabel':'singular_value_index',
            };     
        #data2 = svg
        #if single plot, data2 = filter menu, data2, and table
        data1_keys = ['experiment_id','gene_id','gene_short_name'
                    ];
        data1_nestkeys = ['gene_short_name'];
        data1_keymap_svg = [];
        svgtype = [];
        svgtile2datamap = [];
        for cnt1,column1 in enumerate(columnValueHeader_O):
            for cnt2,column2 in enumerate(columnValueHeader_O[cnt1:]):
                keymap = {
                'xdata':column1,
                'ydata':column2,
                'serieslabel':'experiment_id',
                'featureslabel':'gene_id',
                'tooltipdata':'gene_id',
                };
                data1_keymap_svg.append([keymap]);
                svgtype.append('pcaplot2d_scores_01');
                svgtile2datamap.append([0]);

        nsvgtable = ddt_container_filterMenuAndChart2dAndTable();
        nsvgtable.make_filterMenuAndChart2dAndTable(
                data_filtermenu=data_O,
                data_filtermenu_keys=data1_keys,
                data_filtermenu_nestkeys=data1_nestkeys,
                data_filtermenu_keymap=data1_keymap_table,
                data_svg_keys=data1_keys,
                data_svg_nestkeys=data1_nestkeys,
                data_svg_keymap=[data1_keymap_svg1,data1_keymap_svg2,data1_keymap_svg3],
                data_table_keys=data1_keys,
                data_table_nestkeys=data1_nestkeys,
                data_table_keymap=data1_keymap_table,
                data_svg=None,
                data_table=None,
                svgtype=svgtype,
                tabletype='responsivetable_01',
                svgx1axislabel='',
                svgy1axislabel='',
                tablekeymap = [data1_keymap_table],
                svgkeymap = data1_keymap_svg,
                formtile2datamap=[0],
                tabletile2datamap=[0],
                svgtile2datamap=svgtile2datamap,
                svgfilters=None,
                svgtileheader='Pair-wise scatter plot',
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