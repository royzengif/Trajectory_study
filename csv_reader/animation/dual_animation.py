import moviepy.editor as mpy
# We use the GIFs generated earlier to avoid recomputing the animations.
clip_mayavi = mpy.VideoFileClip("sinc.gif")
clip_mpl = mpy.VideoFileClip("sinc_mpl.gif").resize(height=clip_mayavi.h)
animation = mpy.clips_array([[clip_mpl, clip_mayavi]])
animation.write_gif("sinc_plot.gif", fps=20)
