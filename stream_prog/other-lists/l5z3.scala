object l5z3 {
  import scala.io._
  import scala.util.hashing.MurmurHash3
  
  def main(args:Array[String]):Unit = {

        if (args.length>0)
        {
          val file = args(0)
          val fileSource = Source.fromFile(file)
          val chars=fileSource.mkString
     
          val goodExample=chars.sliding(24,1).find(x => (MurmurHash3.stringHash(x) == 320915200)) match {
                case Some(x) => println(x)
                case None => println("The phrase was not found.")
              }
          val badExample=chars.sliding(24,1).find(x => (MurmurHash3.stringHash(x) == 1)) match {
                case Some(x) => println(x)
                case None => println("The phrase was not found.")
              }
          fileSource.close

        }
        else println("no file")
      }

}
