import Element.elem
object Rectangle {
  val space = elem(" ")
  val corner = elem("*")
  def rectangle(width: Int, height: Int): Element = {

    def verticalBar = elem('|', 1, height-2)
    def horizontalBar = elem('=', width-2, 1)
    def spaceBar = elem(' ', width-2, 1)

    var rec = horizontalBar

    val range = 1 to height-2
    for (i <- range) {rec = rec above spaceBar}


    (corner above verticalBar above corner) beside (rec above horizontalBar) beside (corner above verticalBar above corner)

  }
  def main(args: Array[String]) = {
    val width = args(0).toInt
    val height = args(1).toInt

    println(rectangle(width, height))
  }
}