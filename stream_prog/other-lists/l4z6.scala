object l4z6 {
  import java.net.URL
  import java.util.zip.GZIPInputStream
  import scala.io.Source
  
  def main(args:Array[String]):Unit = {
  
    val genURL = "https://ftp.ncbi.nih.gov/genomes/refseq/"
    val species= "bacteria/Escherichia_coli/reference/GCF_000005845.2_ASM584v2/"
    val dna = "GCF_000005845.2_ASM584v2_genomic.fna.gz"
    val fileURL= new URL(genURL+species+dna)
    val is = fileURL.openStream()
    val gz = new GZIPInputStream(is)
    val seqDNA = Source.fromInputStream(gz).getLines().drop(1).mkString("")
   
    val res = seqDNA
          .grouped(3)
          .toList
          .filter(x => x.toString.size > 1)
          .groupBy(identity)
          .mapValues(_.size)
          .toList
          .sortBy(_._1)
          .grouped(4).toList
    println(res.map(_.mkString(" ")).mkString("\n"))
  }
}


