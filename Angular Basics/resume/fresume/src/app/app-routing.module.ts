import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path:'landing',
    loadChildren: ()=>import("./modules/landing/landing.module").then(x=>x.LandingModule)
  },
  {
    path:'',
    pathMatch: 'full',
    redirectTo: '/landing'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
