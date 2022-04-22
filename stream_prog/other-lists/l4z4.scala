object l4z4 {
  import scala.io._
  def main(args:Array[String]):Unit = {

        if (args.length>0)
        {
          val file = args(0)
          val quantity = args(1)
          val fileSource = Source.fromFile(file)
          val words=fileSource.mkString
          .split("\\W+")
          .map(_.toLowerCase())
          .groupBy(identity)
          .mapValues(_.size)
          .toList
          .sortBy(_._2)
          .reverse
          .take(quantity.toInt)
          
          fileSource.close
          println(words)
          
        }
        else println("no file")
      }

}


