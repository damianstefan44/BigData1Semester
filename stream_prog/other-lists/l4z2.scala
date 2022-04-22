object l4z2 {
  import scala.io._
  def main(args:Array[String]):Unit = {

        if (args.length>0)
        {
          val file = args(0)
          val fileSource = Source.fromFile(file)
          val words=fileSource.mkString.split("\\W+").map(_.toLowerCase()).distinct
          fileSource.close
          println("number of distinct words: " + words.length)
        }
        else println("no file")
      }

}
