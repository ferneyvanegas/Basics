import { Component, OnInit } from '@angular/core';
import { faPersonDigging } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-education',
  templateUrl: './education.component.html',
  styleUrls: ['./education.component.css']
})
export class EducationComponent implements OnInit {
  faPersonDigging = faPersonDigging;

  constructor() { }

  ngOnInit(): void {
  }

}
