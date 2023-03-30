import { Component, OnInit } from '@angular/core';
import { faBrain } from '@fortawesome/free-solid-svg-icons';
import { faUsers } from '@fortawesome/free-solid-svg-icons';
import { faVolumeHigh } from '@fortawesome/free-solid-svg-icons';
import { faUserGraduate } from '@fortawesome/free-solid-svg-icons';
import { faHandshake } from '@fortawesome/free-solid-svg-icons';
import { faBook } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-soft-skills',
  templateUrl: './soft-skills.component.html',
  styleUrls: ['./soft-skills.component.css']
})
export class SoftSkillsComponent implements OnInit {
  faBrain = faBrain;
  faUsers = faUsers;
  faVolumeHigh = faVolumeHigh;
  faUserGraduate = faUserGraduate;
  faHandshake = faHandshake;
  faBook = faBook;

  constructor() { }

  ngOnInit(): void {
  }

}
