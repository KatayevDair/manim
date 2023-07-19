%%manim -ql --renderer=cairo asd
#работает в юпитере
# %%manim -ql -gpu PointPlacement

class asd(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 14],
            y_range=[0, 8],
            x_length=12,
            y_length=6,
            tips=True,
        )
        self.play(axes.animate.shift(np.array([-4,  2,  0])).scale(0.5))

        self.add(axes)
        self.wait(2)

        error_formula1 = MathTex('\mathrm{y}_{\t{true_1}} - \mathrm{y}_{\t{pred_1}}',
                         font_size=30).shift(np.array([-4,  -1,  0]))#.move_to([0, -1, 0])#.next_to(axes, np.array([0, -3 ,  0. ]), aligned_edge=OUT)
        error_formula2 = MathTex('+ \mathrm{y}_{\t{true_2}} - \mathrm{y}_{\t{pred_2}}',
                                 font_size=30).next_to(error_formula1, 0.8*RIGHT)
        error_formula3 = MathTex('+ \cdots',
                                 font_size=30).next_to(error_formula2, 0.8*RIGHT)
        error_formula4 = MathTex('+\mathrm{y}_{\t{true_{n-1}}} - \mathrm{y}_{\t{pred_{n-1}}}',
                                 font_size=30).next_to(error_formula3, 0.8*RIGHT)
        error_formula5 = MathTex('+ \mathrm{y}_{\t{true_n}} - \mathrm{y}_{\t{pred_n}}',
                                 font_size=30).next_to(error_formula4, 0.8*RIGHT)
        errors_to_transform = VGroup(error_formula1, error_formula2, error_formula3,
                               error_formula4, error_formula5)
        error_formula6 = MathTex('\left( \mathrm{y}_{\t{true_1}}  - \mathrm{y}_{\t{pred_1}}\\right)^{2} + \left(\mathrm{y}_{\t{true_1}} - \mathrm{y}_{\t{pred_1}}\\right)^{2} + \ldots  + \left(\mathrm{y}_{\t{true_{n-1}}} - \mathrm{y}_{\t{pred_{n-1}}}\\right)^{2} + \left(\mathrm{y}_{\t{true_n}} - \mathrm{y}_{\t{pred_n}}\\right)^{2}',
                             font_size=30).shift(np.array([0,  -1,  0]))
        error_formula7 = MathTex('\\frac{\left( \mathrm{y}_{\t{true_1}}  - \mathrm{y}_{\t{pred_1}}\\right)^{2} + \left(\mathrm{y}_{\t{true_1}} - \mathrm{y}_{\t{pred_1}}\\right)^{2} + \ldots  + \left(\mathrm{y}_{\t{true_{n-1}}} - \mathrm{y}_{\t{pred_{n-1}}}\\right)^{2} + \left(\mathrm{y}_{\t{true_n}} - \mathrm{y}_{\t{pred_n}}\\right)^{2}}{n}',
                                 font_size=30).shift(np.array([0,  -1,  0]))
        error_formula8 = MathTex(r'\sqrt{\frac{\left( \mathrm{y}_{\text{true 1}}  - \mathrm{y}_{\text{pred 1}}\right)^{2} + \left(\mathrm{y}_{\text{true 1}} - \mathrm{y}_{\text{pred 1}}\right)^{2} + \ldots  + \left(\mathrm{y}_{\text{true n-1}} - \mathrm{y}_{\text{pred n-1}}\right)^{2} + \left(\mathrm{y}_{\text{true n}} - \mathrm{y}_{\text{pred n}}\right)^{2}}{n}}',
                                 font_size=30).shift(np.array([0,  -1,  0]))
        error_formula9 = MathTex(r'\sqrt{\sum_{i=1}^{n}\frac{(y_\text{true i} - y_\text{pred i})^{2}}{n}}',
                                 font_size=30).shift(np.array([0,  -1,  0]))
        
        mse = MathTex('MSE =', font_size=30).next_to(error_formula6, np.array([-1, 0,  0. ]), aligned_edge=OUT)
        mse_not_equal = MathTex('MSE ', font_size=30).next_to(error_formula6, np.array([-1, 0,  0. ]), aligned_edge=OUT)
        rmse = MathTex('RMSE =', font_size=30).next_to(error_formula9, np.array([-1, 0,  0. ]), aligned_edge=OUT)
        
        
        rmse = MathTex('RMSE =', font_size=30).next_to(error_formula9, np.array([-1, 0,  0. ]), aligned_edge=OUT)
#         self.play(
#                     FadeIn(mse, engine='opengl')
#                  )
#         errors_to_transform = VGroup(error_formula6, mse)
        self.play(
                    Transform(errors_to_transform, error_formula6, engine='opengl')
                 )
        self.wait(3)
        self.remove(error_formula6)
#         self.play(
#                     Transform(mse, mse_not_equal, engine='opengl')
#                  )
#         self.wait(3)
        self.play(
                    Transform(error_formula6, error_formula7, engine='opengl')
                 )
        self.wait(3)
        self.remove(error_formula7)
        self.play(
                    Transform(error_formula7, error_formula8, engine='opengl')
                 )
        self.wait(3)
        self.remove(error_formula8)
        self.play(
                    Transform(error_formula8, error_formula9, engine='opengl')
                 )
#         self.wait(3)
#         self.play(
#                     Transform(mse_not_equal, rmse, engine='opengl')
        self.wait(3)
#                  )
        self.play(FadeIn(rmse))
        self.wait(3)
