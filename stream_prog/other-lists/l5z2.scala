object l5z2 {
  import scala.io._
  import scala.annotation.tailrec
  import scala.util.hashing.MurmurHash3


  def check(s: String, hashValue: Int) : String = {

    @tailrec
    def checkSub(start: Int, end: Int, s: String): String = {
      if (end <= s.length && MurmurHash3.stringHash(s.substring(start,end)) != hashValue) checkSub(start+1, end+1, s)
      else s.substring(start,end)
    }
    checkSub(0, 24, s)
  }


  def main(args:Array[String]):Unit = {

    if (args.length>0)
    {
      val file = args(0)
      val fileSource = Source.fromFile(file)
      val chars=fileSource.mkString
      fileSource.close

      try{
        println(check(chars,320915200))
        println(check(chars,1))
      }
      catch{
        case e: StringIndexOutOfBoundsException => println("The phrase was not found!")
      }

    }
    else println("no file")
  }

}

// input:
// scala l5z3 canterbury/alice29.txt

// output:
// Curiouser and curiouser!
// The phrase was not found!