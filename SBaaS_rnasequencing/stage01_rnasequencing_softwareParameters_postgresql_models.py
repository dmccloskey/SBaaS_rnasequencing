from SBaaS_base.postgresql_orm_base import *
class data_stage01_rnasequencing_bowtieParameters(Base):
    __tablename__ = 'data_stage01_rnasequencing_bowtieParameters'
    id = Column(Integer, Sequence('data_stage01_rnasequencing_bowtieParameters_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    bowtie_version_number = Column(String(25))
    insertsize = Column(Float)
    threads = Column(Integer)
    trim3 = Column(Integer)
    indexes_dir = Column(String(500))
    organism = Column(String(100))
    paired = Column(String(100)) # 'paired', 'unpaired', or 'mixed'
    input_dir = Column(String(500));
    basename = Column(String(100));
    output_dir = Column(String(500));
    bowtie_options = Column(postgresql.JSON);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    #base_input = input_dir + basename
    #base_output = output_dir + basename

    __table_args__ = (
        UniqueConstraint('experiment_id','sample_name','bowtie_version_number','insertsize',
                         'threads','trim3','paired'
                         ),
            )
    def __init__(self, 
                row_dict_I,
                ):
        self.experiment_id=row_dict_I['experiment_id'];
        self.sample_name=row_dict_I['sample_name'];
        self.bowtie_version_number=row_dict_I['bowtie_version_number'];
        self.insertsize=row_dict_I['insertsize'];
        self.threads=row_dict_I['threads'];
        self.trim3=row_dict_I['trim3'];
        self.indexes_dir=row_dict_I['indexes_dir'];
        self.organism=row_dict_I['organism'];
        self.paired=row_dict_I['paired'];
        self.input_dir=row_dict_I['input_dir'];
        self.basename=row_dict_I['basename'];
        self.output_dir=row_dict_I['output_dir'];
        self.bowtie_options=row_dict_I['bowtie_options'];
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];

    def __set__row__(self,
        experiment_id_I,
        sample_name_I,
        bowtie_version_number_I,
        insertsize_I,
        threads_I,
        trim3_I,
        indexes_dir_I,
        organism_I,
        paired_I,
        input_dir_I,
        basename_I,
        output_dir_I,
        bowtie_options_I,
        used__I,
        comment__I):
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.bowtie_version_number=bowtie_version_number_I
        self.insertsize=insertsize_I
        self.threads=threads_I
        self.trim3=trim3_I
        self.indexes_dir=indexes_dir_I
        self.organism=organism_I
        self.paired=paired_I
        self.input_dir=input_dir_I
        self.basename=basename_I
        self.output_dir=output_dir_I
        self.bowtie_options=bowtie_options_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'bowtie_version_number':self.bowtie_version_number,
                'insertsize':self.insertsize,
                'threads':self.threads,
                'trim3':self.trim3,
                'indexes_dir':self.indexes_dir,
                'organism':self.organism,
                'paired':self.paired,
                'input_dir':self.input_dir,
                'basename':self.basename,
                'output_dir':self.output_dir,
                'bowtie_options':self.bowtie_options,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
    
class data_stage01_rnasequencing_cufflinksParameters(Base):
    __tablename__ = 'data_stage01_rnasequencing_cufflinksParameters'
    id = Column(Integer, Sequence('data_stage01_rnasequencing_cufflinksParameters_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    cufflinks_version_number = Column(String(25))
    library_type = Column(String(50), default='fr-firststrand')
    threads = Column(Integer)
    indexes_dir = Column(String(500))
    organism = Column(String(100))
    input_dir = Column(String(500));
    basename = Column(String(100));
    output_dir = Column(String(500));
    cufflinks_options = Column(postgresql.JSON);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    #base_input = input_dir + basename
    #base_output = output_dir + basename

    __table_args__ = (
        UniqueConstraint('experiment_id','sample_name','cufflinks_version_number','library_type','threads',
                         ),
            )
    def __init__(self, 
                row_dict_I,
                ):
        self.experiment_id=row_dict_I['experiment_id'];
        self.sample_name=row_dict_I['sample_name'];
        self.cufflinks_version_number=row_dict_I['cufflinks_version_number'];
        self.library_type=row_dict_I['library_type'];
        self.indexes_dir=row_dict_I['indexes_dir'];
        self.organism=row_dict_I['organism'];
        self.input_dir=row_dict_I['input_dir'];
        self.basename=row_dict_I['basename'];
        self.output_dir=row_dict_I['output_dir'];
        self.cufflinks_options=row_dict_I['cufflinks_options'];
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];
        self.threads=row_dict_I['threads'];

    def __set__row__(self,
        experiment_id_I,
        sample_name_I,
        cufflinks_version_number_I,
        library_type_I,
        threads_I,
        indexes_dir_I,
        organism_I,
        input_dir_I,
        basename_I,
        output_dir_I,
        cufflinks_options_I,
        used__I,
        comment__I):
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.cufflinks_version_number=cufflinks_version_number_I
        self.library_type=library_type_I
        self.threads=threads_I
        self.indexes_dir=indexes_dir_I
        self.organism=organism_I
        self.input_dir=input_dir_I
        self.basename=basename_I
        self.output_dir=output_dir_I
        self.cufflinks_options=cufflinks_options_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'cufflinks_version_number':self.cufflinks_version_number,
                'library_type':self.library_type,
                'threads':self.threads,
                'indexes_dir':self.indexes_dir,
                'organism':self.organism,
                'input_dir':self.input_dir,
                'basename':self.basename,
                'output_dir':self.output_dir,
                'cufflinks_options':self.cufflinks_options,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
    
class data_stage01_rnasequencing_cuffdiffParameters(Base):
    
    __tablename__ = 'data_stage01_rnasequencing_cuffdiffParameters'
    id = Column(Integer, Sequence('data_stage01_rnasequencing_cuffdiffParameters_id_seq'), primary_key=True)
    #analysis_id = Column(String(500))
    experiment_id_1 = Column(String(50))
    experiment_id_2 = Column(String(50))
    sample_name_abbreviation_1 = Column(String(100))
    sample_name_abbreviation_2 = Column(String(100))
    cuffdiff_version_number = Column(String(25))
    library_type = Column(String(50), default='fr-firststrand')
    threads = Column(String(100))
    library_norm_method = Column(String(100), default='quartile')
    samples_dir_1 = Column(Text)
    samples_dir_2 = Column(Text)
    indexes_dir = Column(String(500))
    organism = Column(String(100))
    basename = Column(String(100));
    output_dir = Column(String(500));
    fdr_level = Column(Float,default=0.05);
    cuffdiff_options = Column(postgresql.JSON);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        UniqueConstraint('experiment_id_1','experiment_id_2','sample_name_abbreviation_1','sample_name_abbreviation_2',
                         'cuffdiff_version_number','library_type','library_norm_method','fdr_level'
                         ),
            )
    def __init__(self, 
                row_dict_I,
                ):
        self.experiment_id_1=row_dict_I['experiment_id_1'];
        self.experiment_id_2=row_dict_I['experiment_id_2'];
        self.sample_name_abbreviation_1=row_dict_I['sample_name_abbreviation_1'];
        self.sample_name_abbreviation_2=row_dict_I['sample_name_abbreviation_2'];
        self.cuffdiff_version_number=row_dict_I['cuffdiff_version_number'];
        self.threads=row_dict_I['threads'];
        self.library_norm_method=row_dict_I['library_norm_method'];
        self.samples_dir_1=row_dict_I['samples_dir_1'];
        self.samples_dir_2=row_dict_I['samples_dir_2'];
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];
        self.library_type=row_dict_I['library_type'];
        self.indexes_dir=row_dict_I['indexes_dir'];
        self.organism=row_dict_I['organism'];
        self.basename=row_dict_I['basename'];
        self.output_dir=row_dict_I['output_dir'];
        self.fdr_level=row_dict_I['fdr_level'];
        self.cuffdiff_options=row_dict_I['cuffdiff_options'];

    def __set__row__(self,
        #analysis_id_I,
        experiment_id_1_I,
        experiment_id_2_I,
        sample_name_abbreviation_1_I,
        sample_name_abbreviation_2_I,
        cuffdiff_version_number_I,
        library_type_I,
        threads_I,
        library_norm_method_I,
        samples_dir_1_I,
        samples_dir_2_I,
        indexes_dir_I,
        organism_I,
        basename_I,
        output_dir_I,
        fdr_level_I,
        cuffdiff_options_I,
        used__I,
        comment__I):
        #self.analysis_id=analysis_id_I
        self.experiment_id_1=experiment_id_1_I
        self.experiment_id_2=experiment_id_2_I
        self.sample_name_abbreviation_1=sample_name_abbreviation_1_I
        self.sample_name_abbreviation_2=sample_name_abbreviation_2_I
        self.cuffdiff_version_number=cuffdiff_version_number_I
        self.library_type=library_type_I
        self.threads=threads_I
        self.library_norm_method=library_norm_method_I
        self.samples_dir_1=samples_dir_1_I
        self.samples_dir_2=samples_dir_2_I
        self.indexes_dir=indexes_dir_I
        self.organism=organism_I
        self.basename=basename_I
        self.output_dir=output_dir_I
        self.fdr_level=fdr_level_I
        self.cuffdiff_options=cuffdiff_options_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                #'analysis_id':self.analysis_id,
                'experiment_id_1':self.experiment_id_1,
                'experiment_id_2':self.experiment_id_2,
                'sample_name_abbreviation_1':self.sample_name_abbreviation_1,
                'sample_name_abbreviation_2':self.sample_name_abbreviation_2,
                'cuffdiff_version_number':self.cuffdiff_version_number,
                'library_type':self.library_type,
                'threads':self.threads,
                'library_norm_method':self.library_norm_method,
                'samples_dir_1':self.samples_dir_1,
                'samples_dir_2':self.samples_dir_2,
                'organism':self.organism,
                'input_dir':self.input_dir,
                'basename':self.basename,
                'output_dir':self.output_dir,
                'fdr_level':self.fdr_level,
                'cuffdiff_options':self.cuffdiff_options,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_rnasequencing_cuffnormParameters(Base):
    
    __tablename__ = 'data_stage01_rnasequencing_cuffnormParameters'
    id = Column(Integer, Sequence('data_stage01_rnasequencing_cuffnormParameters_id_seq'), primary_key=True)
    analysis_id = Column(String(500))
    sample_names = Column(Column(Text))
    cuffdiff_version_number = Column(String(25))
    library_type = Column(String(50), default='fr-firststrand')
    threads = Column(String(100))
    library_norm_method = Column(String(100), default='quartile')
    samples_dirs = Column(Text)
    indexes_dir = Column(String(500))
    organism = Column(String(100))
    output_dir = Column(String(500));
    cuffdiff_options = Column(postgresql.JSON);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        UniqueConstraint('analysis_id',
                         'cuffdiff_version_number','library_type','library_norm_method'
                         ),
            )
    def __init__(self, 
                row_dict_I,
                ):
        self.analysis_id=row_dict_I['analysis_id'];
        self.sample_names=row_dict_I['sample_names'];
        self.cuffdiff_version_number=row_dict_I['cuffdiff_version_number'];
        self.threads=row_dict_I['threads'];
        self.library_norm_method=row_dict_I['library_norm_method'];
        self.samples_dirs=row_dict_I['samples_dirs'];
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];
        self.library_type=row_dict_I['library_type'];
        self.indexes_dir=row_dict_I['indexes_dir'];
        self.organism=row_dict_I['organism'];
        self.output_dir=row_dict_I['output_dir'];
        self.cuffdiff_options=row_dict_I['cuffdiff_options'];

    def __set__row__(self,
        analysis_id_I,
        sample_names_I,
        cuffdiff_version_number_I,
        library_type_I,
        threads_I,
        library_norm_method_I,
        samples_dirs_I,
        indexes_dir_I,
        organism_I,
        output_dir_I,
        cuffdiff_options_I,
        used__I,
        comment__I):
        self.analysis_id=analysis_id_I
        self.sample_names=sample_names_I
        self.cuffdiff_version_number=cuffdiff_version_number_I
        self.library_type=library_type_I
        self.threads=threads_I
        self.library_norm_method=library_norm_method_I
        self.samples_dirs_1=samples_dirs_I
        self.indexes_dir=indexes_dir_I
        self.organism=organism_I
        self.output_dir=output_dir_I
        self.cuffdiff_options=cuffdiff_options_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'analysis_id':self.analysis_id,
                'sample_names':self.sample_names,
                'cuffdiff_version_number':self.cuffdiff_version_number,
                'library_type':self.library_type,
                'threads':self.threads,
                'library_norm_method':self.library_norm_method,
                'samples_dirs':self.samples_dirs,
                'organism':self.organism,
                'input_dir':self.input_dir,
                'output_dir':self.output_dir,
                'cuffdiff_options':self.cuffdiff_options,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())