import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit {

  num:number;
  table = new Array;

  constructor() {
    this.num = 1;
   }

  ngOnInit(): void {
    this.setTableResults();
  }

  public setTableResults(){
    this.table = [];
    for(let x=1; x<11; x++){
      let str = `${this.num} x ${x} = ${this.num * x}`;
      this.table.push(str);
    }
  }

  

}
