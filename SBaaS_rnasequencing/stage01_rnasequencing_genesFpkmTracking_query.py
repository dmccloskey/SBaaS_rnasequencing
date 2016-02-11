#sbaas
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query
#sbaas models
from .stage01_rnasequencing_genesFpkmTracking_postgresql_models import *

class stage01_rnasequencing_genesFpkmTracking_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_rnasequencing_genesFpkmTracking':data_stage01_rnasequencing_genesFpkmTracking,
                        };
        self.set_supportedTables(tables_supported);
    # query data from data_stage01_rnasequencing_genesFpkmTracking
    def get_rows_experimentIDAndSampleName_dataStage01RNASequencingGenesFpkmTracking(self,experiment_id_I,sample_name_I):
        '''Query rows by experiment_id and sample_name'''
        try:
            data = self.session.query(data_stage01_rnasequencing_genesFpkmTracking).filter(
                    data_stage01_rnasequencing_genesFpkmTracking.experiment_id.like(experiment_id_I),
                    data_stage01_rnasequencing_genesFpkmTracking.sample_name.like(sample_name_I),
                    data_stage01_rnasequencing_genesFpkmTracking.used_).all();
            data_O = [];
            for d in data: 
                data_dict = {'id':d.id,
                #'analysis_id':d.analysis_id,
                'experiment_id':d.experiment_id,
                'sample_name':d.sample_name,
                'tracking_id':d.tracking_id,
                'class_code':d.class_code,
                'nearest_ref_id':d.nearest_ref_id,
                'gene_id':d.gene_id,
                'gene_short_name':d.gene_short_name,
                'tss_id':d.tss_id,
                'locus':d.locus,
                'length':d.length,
                'coverage':d.coverage,
                'FPKM':d.FPKM,
                'FPKM_conf_lo':d.FPKM_conf_lo,
                'FPKM_conf_hi':d.FPKM_conf_hi,
                'FPKM_status':d.FPKM_status,
                'used_':d.used_,
                'comment_':d.comment_};
                data_O.append(data_dict);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def add_dataStage01RNASequencingGenesFpkmTracking(self, data_I):
        '''add rows of data_stage01_rnasequencing_fpkmTracking'''
        if data_I:
            for d in data_I:
                try:
                    if not 'used_' in d:
                        d['used_'] = True;
                    if not 'comment_' in d:
                        d['comment_'] = None;
                    data_add = data_stage01_rnasequencing_genesFpkmTracking(d['experiment_id'],
                            d['sample_name'],
                            d['tracking_id'],
                            d['class_code'],
                            d['nearest_ref_id'],
                            d['gene_id'],
                            d['gene_short_name'],
                            d['tss_id'],
                            d['locus'],
                            d['length'],
                            d['coverage'],
                            d['FPKM'],
                            d['FPKM_conf_lo'],
                            d['FPKM_conf_hi'],
                            d['FPKM_status'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01RNASequencingGenesFpkmTracking(self,data_I):
        '''update rows of data_stage01_rnasequencing_genesFpkmTracking'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_rnasequencing_genesFpkmTracking).filter(
                           data_stage01_rnasequencing_genesFpkmTracking.id==d['id']).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'tracking_id':d['tracking_id'],
                            'class_code':d['class_code'],
                            'nearest_ref_id':d['nearest_ref_id'],
                            'gene_id':d['gene_id'],
                            'gene_short_name':d['gene_short_name'],
                            'tss_id':d['tss_id'],
                            'locus':d['locus'],
                            'length':d['length'],
                            'coverage':d['coverage'],
                            'FPKM':d['FPKM'],
                            'FPKM_conf_lo':d['FPKM_conf_lo'],
                            'FPKM_conf_hi':d['FPKM_conf_hi'],
                            'FPKM_status':d['FPKM_status'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def reset_dataStage01_rnasequencing_genesFpkmTracking(self,experiment_id_I = None, sample_names_I=[]):
        try:
            if experiment_id_I and sample_names_I:
                for sn in sample_names_I:
                    reset = self.session.query(data_stage01_rnasequencing_genesFpkmTracking).filter(
                        data_stage01_rnasequencing_genesFpkmTracking.experiment_id.like(experiment_id_I),
                        data_stage01_rnasequencing_genesFpkmTracking.sample_name.like(sn)).delete(synchronize_session=False);
            elif experiment_id_I:
                reset = self.session.query(data_stage01_rnasequencing_genesFpkmTracking).filter(data_stage01_rnasequencing_genesFpkmTracking.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_rnasequencing_genesFpkmTracking).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage01_rnasequencing_genesFpkmTracking(self):
        try:
            data_stage01_rnasequencing_genesFpkmTracking.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_rnasequencing_genesFpkmTracking(self):
        try:
            data_stage01_rnasequencing_genesFpkmTracking.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);