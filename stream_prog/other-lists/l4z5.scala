object l4z5 {
  import scala.io._
  def main(args:Array[String]):Unit = {

        if (args.length>0)
        {
          val file1 = args(0)
          val file2 = args(1)
          val fileSource1 = Source.fromFile(file1)
          val words1=fileSource1.mkString
          .split("\\W+")
          .map(_.toLowerCase())
          .distinct
          .toList   
      
          fileSource1.close
          
          val fileSource2 = Source.fromFile(file2)
          val words2=fileSource2.mkString
          .split("\\W+")
          .map(_.toLowerCase())
          .distinct
          .toList
          fileSource2.close
          
          val res = words1.diff(words2).size
          println(res)
          
        }
        else println("no file")
      }

}


