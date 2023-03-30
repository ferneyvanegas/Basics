import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LandingRoutingModule } from './landing-routing.module';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

// Componentes
import { LandingComponent } from './landing.component';
import { NavComponent } from './nav/nav.component';
import { ProfileComponent } from './profile/profile.component';
import { SoftSkillsComponent } from './soft-skills/soft-skills.component';
import { TechSkillsComponent } from './tech-skills/tech-skills.component';
import { EducationComponent } from './education/education.component';
import { WExperienceComponent } from './w-experience/w-experience.component';


@NgModule({
  declarations: [
    NavComponent,
    ProfileComponent,
    SoftSkillsComponent,
    TechSkillsComponent,
    EducationComponent,
    WExperienceComponent,
    LandingComponent
  ],
  imports: [
    CommonModule,
    LandingRoutingModule,
    FontAwesomeModule
  ]
})
export class LandingModule { }
