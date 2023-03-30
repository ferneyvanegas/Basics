import { Component, OnInit } from '@angular/core';
import { faGithub, faGoogle, faLinkedin, faWhatsapp } from '@fortawesome/free-brands-svg-icons';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {
  faGithub = faGithub;
  faGoogle = faGoogle;
  faLinkedin = faLinkedin;
  faWhatsapp = faWhatsapp;

  constructor() { }

  ngOnInit(): void {
  }

}
