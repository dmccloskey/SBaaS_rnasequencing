from SBaaS_base.postgresql_orm_base import *

class data_stage01_rnasequencing_geneExpDiff(Base):
    
    __tablename__ = 'data_stage01_rnasequencing_geneExpDiff'
    id = Column(Integer, Sequence('data_stage01_rnasequencing_geneExpDiff_id_seq'), primary_key=True)
    #analysis_id = Column(String(500))
    experiment_id_1 = Column(String(50))
    experiment_id_2 = Column(String(50))
    sample_name_abbreviation_1 = Column(String(100))
    sample_name_abbreviation_2 = Column(String(100))
    test_id = Column(String(100))
    gene_id = Column(String(100))
    gene = Column(String(100))
    sample_1 = Column(String(100))
    sample_2 = Column(String(100))
    status = Column(String(100))
    value_1 = Column(Float);
    value_2 = Column(Float);
    fold_change_log2 = Column(Float);
    test_stat = Column(String(100))
    p_value = Column(Float); # uncorrected p-value
    q_value = Column(Float); # FDR corrected p-value
    significant = Column(String(100)) #Yes/No
    #library_norm_method = Column(String(100))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        UniqueConstraint('experiment_id_1',
                         'experiment_id_2',
                         'sample_name_abbreviation_1',
                         'sample_name_abbreviation_2',
                         'gene_id',
                         #'library_norm_method'
                         ),
            )
    def __init__(self, 
                row_dict_I,
                ):
        self.experiment_id_1=row_dict_I['experiment_id_1'];
        self.experiment_id_2=row_dict_I['experiment_id_2'];
        self.sample_name_abbreviation_1=row_dict_I['sample_name_abbreviation_1'];
        self.sample_name_abbreviation_2=row_dict_I['sample_name_abbreviation_2'];
        self.test_id=row_dict_I['test_id'];
        self.gene_id=row_dict_I['gene_id'];
        self.gene=row_dict_I['gene'];
        self.sample_1=row_dict_I['sample_1'];
        self.sample_2=row_dict_I['sample_2'];
        self.status=row_dict_I['status'];
        self.value_1=row_dict_I['value_1'];
        self.value_2=row_dict_I['value_2'];
        self.fold_change_log2=row_dict_I['fold_change_log2'];
        self.test_stat=row_dict_I['test_stat'];
        self.p_value=row_dict_I['p_value'];
        self.q_value=row_dict_I['q_value'];
        self.significant=row_dict_I['significant'];
        #self.library_norm_method=row_dict_I['library_norm_method'];
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];

    def __set__row__(self,
        #analysis_id_I,
        experiment_id_1_I,
        experiment_id_2_I,
        sample_name_abbreviation_1_I,
        sample_name_abbreviation_2_I,
        test_id_I,
        gene_id_I,
        gene_I,
        sample_1_I,
        sample_2_I,
        status_I,
        value_1_I,
        value_2_I,
        fold_change_log2_I,
        test_stat_I,
        p_value_I,
        q_value_I,
        significant_I,
        #library_norm_method_I,
        used__I,
        comment__I):
        #self.analysis_id=analysis_id_I
        self.experiment_id_1=experiment_id_1_I
        self.experiment_id_2=experiment_id_2_I
        self.sample_name_abbreviation_1=sample_name_abbreviation_1_I
        self.sample_name_abbreviation_2=sample_name_abbreviation_2_I
        self.test_id=test_id_I
        self.gene_id=gene_id_I
        self.gene=gene_I
        self.sample_1=sample_1_I
        self.sample_2=sample_2_I
        self.status=status_I
        self.value_1=value_1_I
        self.value_2=value_2_I
        self.fold_change_log2=fold_change_log2_I
        self.test_stat=test_stat_I
        self.p_value=p_value_I
        self.q_value=q_value_I
        self.significant=significant_I
        #self.library_norm_method=library_norm_method_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                #'analysis_id':self.analysis_id,
                'experiment_id_1':self.experiment_id_1,
                'experiment_id_2':self.experiment_id_2,
                'sample_name_abbreviation_1':self.sample_name_abbreviation_1,
                'sample_name_abbreviation_2':self.sample_name_abbreviation_2,
                'test_id':self.test_id,
                'gene_id':self.gene_id,
                'gene':self.gene,
                'sample_1':self.sample_1,
                'sample_2':self.sample_2,
                'status':self.status,
                'value_1':self.value_1,
                'value_2':self.value_2,
                'fold_change_log2':self.fold_change_log2,
                'test_stat':self.test_stat,
                'p_value':self.p_value,
                'q_value':self.q_value,
                'significant':self.significant,
                #'library_norm_method':self.library_norm_method,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
    
class data_stage01_rnasequencing_geneExpDiffFpkmTracking(Base):
    #fpkm = fragments per kilobase of transcript
    __tablename__ = 'data_stage01_rnasequencing_geneExpDiffFpkmTracking'
    id = Column(Integer, Sequence('data_stage01_rnasequencing_geneExpDiffFpkmTracking_id_seq'), primary_key=True)
    analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    tracking_id = Column(String(100))
    class_code = Column(String(100))
    nearest_ref_id = Column(String(100))
    gene_id = Column(String(100))
    gene_short_name = Column(String(100))
    tss_id = Column(String(100))
    locus = Column(String(100))
    length = Column(Float);
    coverage = Column(Float);
    FPKM = Column(Float);
    FPKM_conf_lo = Column(Float);
    FPKM_conf_hi = Column(Float);
    FPKM_status = Column(String(100))
    #library_norm_method = Column(String(100))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        UniqueConstraint('experiment_id','sample_name_abbreviation','gene_id','analysis_id',
                         #'library_norm_method'
                         ),
            )
    def __init__(self, 
                row_dict_I,
                ):
        self.analysis_id=row_dict_I['analysis_id'];
        self.comment_=row_dict_I['comment_'];
        self.used_=row_dict_I['used_'];
        self.FPKM_status=row_dict_I['FPKM_status'];
        self.FPKM_conf_hi=row_dict_I['FPKM_conf_hi'];
        self.FPKM_conf_lo=row_dict_I['FPKM_conf_lo'];
        self.FPKM=row_dict_I['FPKM'];
        self.coverage=row_dict_I['coverage'];
        self.length=row_dict_I['length'];
        self.locus=row_dict_I['locus'];
        self.tss_id=row_dict_I['tss_id'];
        self.gene_short_name=row_dict_I['gene_short_name'];
        self.gene_id=row_dict_I['gene_id'];
        self.nearest_ref_id=row_dict_I['nearest_ref_id'];
        self.class_code=row_dict_I['class_code'];
        self.tracking_id=row_dict_I['tracking_id'];
        self.sample_name_abbreviation=row_dict_I['sample_name_abbreviation'];
        self.experiment_id=row_dict_I['experiment_id'];
        #self.library_norm_method=row_dict_I['library_norm_method'];

    def __set__row__(self,analysis_id_I,
        experiment_id_I,
        sample_name_abbreviation_I,
        tracking_id_I,
        class_code_I,
        nearest_ref_id_I,
        gene_id_I,
        gene_short_name_I,
        tss_id_I,
        locus_I,
        length_I,
        coverage_I,
        FPKM_I,
        FPKM_conf_lo_I,
        FPKM_conf_hi_I,
        FPKM_status_I,
        #library_norm_method_I,
        used__I,
        comment__I):
        self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.tracking_id=tracking_id_I
        self.class_code=class_code_I
        self.nearest_ref_id=nearest_ref_id_I
        self.gene_id=gene_id_I
        self.gene_short_name=gene_short_name_I
        self.tss_id=tss_id_I
        self.locus=locus_I
        self.length=length_I
        self.coverage=coverage_I
        self.FPKM=FPKM_I
        self.FPKM_conf_lo=FPKM_conf_lo_I
        self.FPKM_conf_hi=FPKM_conf_hi_I
        self.FPKM_status=FPKM_status_I
        #self.library_norm_method=library_norm_method_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'analysis_id':self.analysis_id,
                'experiment_id':self.experiment_id,
                'sample_name_abbreviation':self.sample_name_abbreviation,
                'tracking_id':self.tracking_id,
                'class_code':self.class_code,
                'nearest_ref_id':self.nearest_ref_id,
                'gene_id':self.gene_id,
                'gene_short_name':self.gene_short_name,
                'tss_id':self.tss_id,
                'locus':self.locus,
                'length':self.length,
                'coverage':self.coverage,
                'FPKM':self.FPKM,
                'FPKM_conf_lo':self.FPKM_conf_lo,
                'FPKM_conf_hi':self.FPKM_conf_hi,
                'FPKM_status':self.FPKM_status,
                #'library_norm_method':self.library_norm_method,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())