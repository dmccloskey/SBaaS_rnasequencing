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
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        UniqueConstraint('experiment_id_1','experiment_id_2','sample_name_abbreviation_1','sample_name_abbreviation_2','gene_id'
                         ),
            )

    def __init__(self,
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
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())