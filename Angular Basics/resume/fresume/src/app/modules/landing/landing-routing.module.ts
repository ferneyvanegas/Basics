import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EducationComponent } from './education/education.component';

// Componentes
import { LandingComponent } from './landing.component';
import { ProfileComponent } from './profile/profile.component';
import { SoftSkillsComponent } from './soft-skills/soft-skills.component';
import { TechSkillsComponent } from './tech-skills/tech-skills.component';
import { WExperienceComponent } from './w-experience/w-experience.component';

const routes: Routes = [
  {
    path:'',
    component: LandingComponent,
    children:[
      {
        path:'profile',
        component: ProfileComponent
      },
      {
        path:'soft-skills',
        component: SoftSkillsComponent
      },
      {
        path:'tech-skills',
        component: TechSkillsComponent
      },
      {
        path:'education',
        component: EducationComponent
      },
      {
        path:'w-experience',
        component: WExperienceComponent
      }
    ]
  },
  {
    path:'**',
    redirectTo: ''
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LandingRoutingModule { }
