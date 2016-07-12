from SBaaS_base.postgresql_orm_base import *

class data_stage01_rnasequencing_genesCountTable(Base):
    #fpkm = fragments per kilobase of transcript
    __tablename__ = 'data_stage01_rnasequencing_genesCountTable'
    id = Column(Integer, Sequence('data_stage01_rnasequencing_genesCountTable_id_seq'), primary_key=True)
    analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    tracking_id = Column(String(100))
    class_code = Column(String(100))
    nearest_ref_id = Column(String(100))
    gene_id = Column(String(100))
    gene_short_name = Column(String(100))
    tss_id = Column(String(100))
    locus = Column(String(100))
    length = Column(Float);
    value = Column(Float);
    value_units = Column(String(50));
    #library_norm_method = Column(String(100))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        UniqueConstraint('analysis_id','experiment_id','sample_name',
                         'gene_id','value_units',
                         #'library_norm_method'
                         ),
            )
    def __init__(self, 
                row_dict_I,
                ):
        self.comment_=row_dict_I['comment_'];
        self.used_=row_dict_I['used_'];
        self.analysis_id=row_dict_I['analysis_id'];
        self.value_units=row_dict_I['value_units'];
        self.value=row_dict_I['value'];
        self.length=row_dict_I['length'];
        self.locus=row_dict_I['locus'];
        self.tss_id=row_dict_I['tss_id'];
        self.gene_short_name=row_dict_I['gene_short_name'];
        self.gene_id=row_dict_I['gene_id'];
        self.nearest_ref_id=row_dict_I['nearest_ref_id'];
        self.class_code=row_dict_I['class_code'];
        self.tracking_id=row_dict_I['tracking_id'];
        self.sample_name=row_dict_I['sample_name'];
        self.experiment_id=row_dict_I['experiment_id'];
        #self.library_norm_method=row_dict_I['library_norm_method'];

    def __set__row__(self,
        analysis_id_I,
        experiment_id_I,
        sample_name_I,
        tracking_id_I,
        class_code_I,
        nearest_ref_id_I,
        gene_id_I,
        gene_short_name_I,
        tss_id_I,
        locus_I,
        length_I,
        value_I,
        value_units_I,
        #library_norm_method_I,
        used__I,
        comment__I):
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.tracking_id=tracking_id_I
        self.class_code=class_code_I
        self.nearest_ref_id=nearest_ref_id_I
        self.gene_id=gene_id_I
        self.gene_short_name=gene_short_name_I
        self.tss_id=tss_id_I
        self.locus=locus_I
        self.length=length_I
        self.value=value_I
        self.value_units=value_units_I
        self.analysis_id=analysis_id_I
        #self.library_norm_method=library_norm_method_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'tracking_id':self.tracking_id,
                'class_code':self.class_code,
                'nearest_ref_id':self.nearest_ref_id,
                'gene_id':self.gene_id,
                'gene_short_name':self.gene_short_name,
                'tss_id':self.tss_id,
                'locus':self.locus,
                'length':self.length,
                'value':self.value,
                'value_units':self.value_units,
                'analysis_id':self.analysis_id,
                #'library_norm_method':self.library_norm_method,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())