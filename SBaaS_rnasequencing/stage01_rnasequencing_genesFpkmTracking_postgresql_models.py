from SBaaS_base.postgresql_orm_base import *

class data_stage01_rnasequencing_genesFpkmTracking(Base):
    #fpkm = fragments per kilobase of transcript
    __tablename__ = 'data_stage01_rnasequencing_genesFpkmTracking'
    id = Column(Integer, Sequence('data_stage01_rnasequencing_genesFpkmTracking_id_seq'), primary_key=True)
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
    coverage = Column(Float);
    FPKM = Column(Float);
    FPKM_conf_lo = Column(Float);
    FPKM_conf_hi = Column(Float);
    FPKM_status = Column(String(100))
    #library_norm_method = Column(String(100))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        UniqueConstraint('experiment_id','sample_name','gene_id',
                         #'library_norm_method'
                         ),
            )
    def __init__(self, 
                row_dict_I,
                ):
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
        self.sample_name=row_dict_I['sample_name'];
        self.experiment_id=row_dict_I['experiment_id'];
        #self.library_norm_method=row_dict_I['library_norm_method'];

    def __set__row__(self,
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
        coverage_I,
        FPKM_I,
        FPKM_conf_lo_I,
        FPKM_conf_hi_I,
        FPKM_status_I,
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