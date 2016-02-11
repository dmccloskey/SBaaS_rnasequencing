﻿#sbaas
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query
#sbaas models
from .stage01_rnasequencing_analysis_postgresql_models import *

class stage01_rnasequencing_analysis_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_rnasequencing_analysis':data_stage01_rnasequencing_analysis,
                        };
        self.set_supportedTables(tables_supported);
    # query data from data_stage01_rnasequencing_analysis
    def get_analysis_analysisID_dataStage01RNASequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_rnasequencing_analysis).filter(
                    data_stage01_rnasequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_rnasequencing_analysis.used_.is_(True)).all();
            analysis_id_O = []
            experiment_id_O = []
            sample_name_abbreviation_O = []
            sample_name_O = []
            analysis_type_O = []
            analysis_O = {};
            if data: 
                for d in data:
                    analysis_id_O.append(d.analysis_id);
                    experiment_id_O.append(d.experiment_id);
                    sample_name_abbreviation_O.append(d.sample_name_abbreviation);
                    sample_name_O.append(d.sample_name);
                    analysis_type_O.append(d.analysis_type);
                analysis_id_O = list(set(analysis_id_O))
                experiment_id_O = list(set(experiment_id_O))
                sample_name_abbreviation_O = list(set(sample_name_abbreviation_O))
                sample_name_O = list(set(sample_name_O))
                analysis_type_O = list(set(analysis_type_O))
                analysis_O={
                        'analysis_id':analysis_id_O,
                        'experiment_id':experiment_id_O,
                        'sample_name_abbreviation':sample_name_abbreviation_O,
                        'sample_name':sample_name_O,
                        'analysis_type':analysis_type_O};
                
            return analysis_O;
        except SQLAlchemyError as e:
            print(e);
    def get_experimentIDAndSampleNameAbbreviation_analysisID_dataStage01RNASequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_rnasequencing_analysis.experiment_id,
                    data_stage01_rnasequencing_analysis.sample_name_abbreviation).filter(
                    data_stage01_rnasequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_rnasequencing_analysis.used_.is_(True)).group_by(
                    data_stage01_rnasequencing_analysis.experiment_id,
                    data_stage01_rnasequencing_analysis.sample_name_abbreviation).order_by(
                    data_stage01_rnasequencing_analysis.experiment_id.asc(),
                    data_stage01_rnasequencing_analysis.sample_name_abbreviation.asc()).all();
            experiment_id_O = []
            sample_name_abbreviation_O = []
            if data: 
                for d in data:
                    experiment_id_O.append(d.experiment_id);
                    sample_name_abbreviation_O.append(d.sample_name_abbreviation);                
            return  experiment_id_O,sample_name_abbreviation_O;
        except SQLAlchemyError as e:
            print(e);
    def get_experimentIDAndSampleName_analysisID_dataStage01RNASequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_rnasequencing_analysis.experiment_id,
                    data_stage01_rnasequencing_analysis.sample_name).filter(
                    data_stage01_rnasequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_rnasequencing_analysis.used_.is_(True)).group_by(
                    data_stage01_rnasequencing_analysis.experiment_id,
                    data_stage01_rnasequencing_analysis.sample_name).order_by(
                    data_stage01_rnasequencing_analysis.experiment_id.asc(),
                    data_stage01_rnasequencing_analysis.sample_name.asc()).all();
            experiment_id_O = []
            sample_name_O = []
            if data: 
                for d in data:
                    experiment_id_O.append(d.experiment_id);
                    sample_name_O.append(d.sample_name);                
            return  experiment_id_O,sample_name_O;
        except SQLAlchemyError as e:
            print(e);
    def get_experimentIDAndSampleNameAndTimePoint_analysisID_dataStage01RNASequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_rnasequencing_analysis.experiment_id,
                    data_stage01_rnasequencing_analysis.sample_name,
                    data_stage01_rnasequencing_analysis.time_point).filter(
                    data_stage01_rnasequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_rnasequencing_analysis.used_.is_(True)).group_by(
                    data_stage01_rnasequencing_analysis.experiment_id,
                    data_stage01_rnasequencing_analysis.sample_name,
                    data_stage01_rnasequencing_analysis.time_point).order_by(
                    data_stage01_rnasequencing_analysis.experiment_id.asc(),
                    data_stage01_rnasequencing_analysis.sample_name.asc(),
                    data_stage01_rnasequencing_analysis.time_point.asc()).all();
            experiment_id_O = []
            sample_name_O = []
            time_point_O = []
            if data: 
                for d in data:
                    experiment_id_O.append(d.experiment_id);
                    sample_name_O.append(d.sample_name);    
                    time_point_O.append(d.time_point);              
            return  experiment_id_O,sample_name_O,time_point_O;
        except SQLAlchemyError as e:
            print(e);
    def get_experimentIDAndSampleNameAbbreviationAndSampleNameAndTimePoint_analysisID_dataStage01RNASequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_rnasequencing_analysis.experiment_id,
                    data_stage01_rnasequencing_analysis.sample_name_abbreviation,
                    data_stage01_rnasequencing_analysis.sample_name,
                    data_stage01_rnasequencing_analysis.time_point).filter(
                    data_stage01_rnasequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_rnasequencing_analysis.used_.is_(True)).group_by(
                    data_stage01_rnasequencing_analysis.experiment_id,
                    data_stage01_rnasequencing_analysis.sample_name_abbreviation,
                    data_stage01_rnasequencing_analysis.sample_name,
                    data_stage01_rnasequencing_analysis.time_point).order_by(
                    data_stage01_rnasequencing_analysis.experiment_id.asc(),
                    data_stage01_rnasequencing_analysis.sample_name_abbreviation.asc(),
                    data_stage01_rnasequencing_analysis.sample_name.asc(),
                    data_stage01_rnasequencing_analysis.time_point.asc()).all();
            experiment_id_O = []
            sample_name_abbreviation_O = []
            sample_name_O = []
            time_point_O = []
            if data: 
                for d in data:
                    experiment_id_O.append(d.experiment_id);
                    sample_name_abbreviation_O.append(d.sample_name_abbreviation); 
                    sample_name_O.append(d.sample_name);    
                    time_point_O.append(d.time_point);              
            return  experiment_id_O,sample_name_abbreviation_O,sample_name_O,time_point_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_analysisID_dataStage01RNASequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_rnasequencing_analysis).filter(
                    data_stage01_rnasequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_rnasequencing_analysis.used_.is_(True)).all();
            analysis_O = [];
            if data: 
                for d in data:
                    analysis_O.append({
                        'analysis_id':d.analysis_id,
                        'experiment_id':d.experiment_id,
                        'sample_name_abbreviation':d.sample_name_abbreviation,
                        'sample_name':d.sample_name,
                        'analysis_type':d.analysis_type});
                
            return analysis_O;
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage01RNASequencingAnalysis(self, data_I):
        '''add rows of data_stage01_rnasequencing_analysis'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_rnasequencing_analysis(d['analysis_id'],
                            d['experiment_id'],
                            d['sample_name_abbreviation'],
                            d['sample_name'],
                            d['time_point'],
                            d['analysis_type'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage01RNASequencingAnalysis(self,data_I):
        '''update rows of data_stage01_rnasequencing_lineage'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_rnasequencing_analysis).filter(
                           data_stage01_rnasequencing_analysis.id==d['id']).update(
                            {'analysis_id':d['analysis_id'],
                            'experiment_id':d['experiment_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'sample_name':d['sample_name'],
                            'time_point':d['time_point'],
                            'analysis_type':d['analysis_type'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def drop_dataStage01_rnasequencing_analysis(self):
        try:
            data_stage01_rnasequencing_analysis.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_rnasequencing_analysis(self):
        try:
            data_stage01_rnasequencing_analysis.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_rnasequencing_analysis(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage01_rnasequencing_analysis).filter(data_stage01_rnasequencing_analysis.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_rnasequencing_analysis).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);