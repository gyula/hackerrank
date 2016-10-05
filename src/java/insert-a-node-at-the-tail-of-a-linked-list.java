Node Insert(Node head,int data) {
  if ( head == null) {
      head.data = data;
      head.next = null;
  } else {
      Node iter = head;
      Node last = new Node();
      last.data = data;
      last.next = null;
      while ( iter.next != null) {
          iter = iter.next;
      }
      iter.next = last;
  }
  return head;
}
