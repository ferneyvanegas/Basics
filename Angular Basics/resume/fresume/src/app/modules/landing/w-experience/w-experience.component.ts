import { Component, OnInit } from '@angular/core';
import { faPersonDigging } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-w-experience',
  templateUrl: './w-experience.component.html',
  styleUrls: ['./w-experience.component.css']
})
export class WExperienceComponent implements OnInit {
  faPersonDigging = faPersonDigging;

  constructor() { }

  ngOnInit(): void {
  }

}
