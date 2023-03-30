import { Component, OnInit } from '@angular/core';
import { faPersonDigging } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-tech-skills',
  templateUrl: './tech-skills.component.html',
  styleUrls: ['./tech-skills.component.css']
})
export class TechSkillsComponent implements OnInit {
  faPersonDigging = faPersonDigging;

  constructor() { }

  ngOnInit(): void {
  }

}
