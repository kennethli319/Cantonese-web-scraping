wget https://downloads.tatoeba.org/exports/per_language/yue/yue_sentences.tsv.bz2
bunzip2 yue_sentences.tsv.bz2
wget https://downloads.tatoeba.org/exports/sentences_with_audio.tar.bz2
tar -xvjf sentences_with_audio.tar.bz2
rm sentences_with_audio.tar.bz2
