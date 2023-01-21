# gene_expression
[ARCHS4](https://github.com/MaayanLab/archs4) is the biggest gene expression dataset that aggregates the vast majority of the published RNA-seq data for human and mouse. The results are published in https://www.nature.com/articles/s41467-018-03751-6 and form a valuable resource for designing experiments that would help draw insights from the human genome Its latest version provides over 620K biosmaples for over 60K genes.
## create_multi_hot_encoded_biosample_annotation.py:
We downloaded all the expression files for all tissue types and cell lines from https://maayanlab.cloud/archs4/ and created a multi-hot encoded version for all the biosamples for which there exists an annotation. There are 121,983 such biosamples. 
## normalization:
The expression values in the data are raw read counts from the Kallisto sequence aligner. The process produces readcounts that are neither similarly distributed for each biosmaple, nor do they account for sequencing depth for the length of a gene. To rectify both the issue we performed two steps:
### Quantile Normalization:
We added a pseudo-count of 1 to all the expression values and performed log transformation, followed by quantile normalization, to force the expression values to have similar distribution.
### Gene length Normalization:
For each gene, we used the length of its longest transcript from the [GENCODE] (https://www.gencodegenes.org/) to divide the expression values from each biosample.
## information_metrics:
The ranking metrics modified for gene-expression data.
### The Signal Metric:
To approximate signal to noise ratio for gene expression, we modified the metric to get the 95 percentile expression value for each gene, making the metric more robust to noise errors from both ends, given the high dimensionality of the data. The expression values from the low expressed biosamples for each gene present a near constant noise level for each gene, likewise the highest expression values are prone to errors from the Kallisto aligner leading to misjudgement in the relative expression values of biosamples within a gene. The 95 percentile expression value hence is a better measure of signal contained in a gene.
### Mean Cosine Similarity:
We identified 100 biosamples around the 95 percentile signal value for each gene, and computed the mean of the cosine similarity among them.
## classification:
Most biosaples in the dataset do not have a cell-line or a tissue-type annotation. We use a Random Forest Classifier to classify them. We use ~120K labeleld biosamples to train, validate and test the model.
## GAN_rare_labels:
Classification is better if labels with only a meagre training examples are removed. However, in this case the rare labels, for example brain biosamples are scarce and difficult to obtain. So, data augmentation techniques are crucial to still be able to build a prediction model. Here, I use a GAN (generative adversarial network) to generate synthetic examples to simulate gene-expression of biosamples from brain. 
