import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'table',
    loadChildren: ()=>import('./modules/numerics/numerics.module').then(x=>x.NumericsModule)
  },
  {
    path: '',
    pathMatch: 'full',
    redirectTo: '/table'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
