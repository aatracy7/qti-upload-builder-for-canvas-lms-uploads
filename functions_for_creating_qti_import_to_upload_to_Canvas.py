#Note that some ids are currently repeated. They do not cause problems with imports, but would eventually be nice to polish...

def create_assignment_specifications(title_of_assignment):
    first_part_of_assignment = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
    <questestinterop xmlns=\"http://www.imsglobal.org/xsd/ims_qtiasiv1p2\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd\">
    <assessment ident=\"ge5319f015006e41be4bbf9e8c7d3e89a\" title=\"{title_of_assignment}\">
        <qtimetadata>
        <qtimetadatafield>
            <fieldlabel>cc_maxattempts</fieldlabel>
            <fieldentry>1</fieldentry>
        </qtimetadatafield>
        </qtimetadata>
        <section ident=\"root_section\">"""
    with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','w') as f:
      f.write(first_part_of_assignment)
def add_fill_in_the_blank(id=id):
    id += 1
    text_only_question = f"""<item ident=\"{id}\" title="Question">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>fill_in_multiple_blanks_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>1.0</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>original_answer_ids</fieldlabel>
              <fieldentry>2402</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>g2016d50a7e56789d68ab7febe23efdad</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">&lt;div&gt;&lt;p&gt;[Blank]&lt;/p&gt;&lt;/div&gt;</mattext>
          </material>
          <response_lid ident="response_Blank">
            <material>
              <mattext>Blank</mattext>
            </material>
            <render_choice>
              <response_label ident="2402">
                <material>
                  <mattext texttype="text/plain">Hi</mattext>
                </material>
              </response_label>
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
          <respcondition>
            <conditionvar>
              <varequal respident="response_Blank">2402</varequal>
            </conditionvar>
            <setvar varname="SCORE" action="Add">100.00</setvar>
          </respcondition>
        </resprocessing>
      </item>"""
    with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','a') as f:
      f.write(text_only_question)

def add_text_only_question(id=id):
    id += 1
    text_only_question = f"""<item ident=\"{id}\" title=\"Question\">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>text_only_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>0.0</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>original_answer_ids</fieldlabel>
              <fieldentry></fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>gf47b767d37e06559ff801f2d253307ba</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype=\"text/html\"></mattext>
          </material>
        </presentation>
      </item>"""
    with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','a') as f:
      f.write(text_only_question)
    return id




def add_multiple_answer_question(*args,id=id,points=1.0,instruction="&lt;p&gt;Select the correct answer.&lt;/p&gt;",correct=""):
  id += 1
  answers = list(args)
  field_entries = ""
  for i in range(len(answers)):
    if (i + 1) == len(answers):
      field_entries += str(i)
    else:
      field_entries += str(i) + ","
  args = sorted(list(args))
  multiple_choice_question = f"""<item ident=\"{id}\" title="Question">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>multiple_answers_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>1.0</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>original_answer_ids</fieldlabel>
              <fieldentry>331,9681,7567,3330,9158,9999</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>g1c14a88a7d09754b38e6a6b464694651</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">&lt;div&gt;&lt;p&gt;REPLACE ME&lt;/p&gt;&lt;/div&gt;</mattext>
          </material>
          <response_lid ident="response1" rcardinality="Multiple">
            <render_choice>
              <response_label ident="331">
                <material>
                  <mattext texttype="text/plain">{args[0]}</mattext>
                </material>
              </response_label>
              <response_label ident="9681">
                <material>
                  <mattext texttype="text/plain">{args[1]}</mattext>
                </material>
              </response_label>
              <response_label ident="7567">
                <material>
                  <mattext texttype="text/plain">{args[2]}</mattext>
                </material>
              </response_label>
              <response_label ident="3330">
                <material>
                  <mattext texttype="text/plain">{args[3]}</mattext>
                </material>
              </response_label>
              <response_label ident="9158">
                <material>
                  <mattext texttype="text/plain">{args[4]}</mattext>
                </material>
              </response_label>
               <response_label ident="9999">
                <material>
                  <mattext texttype="text/plain">{args[5]}</mattext>
                </material>
              </response_label>
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
          <respcondition continue="No">
            <conditionvar>
              <and>
                <not>
                <varequal respident="response1">331</varequal>
                </not>
                <not>
                  <varequal respident="response1">9681</varequal>
                </not>
                <not>
                  <varequal respident="response1">7567</varequal>
                </not>
                <varequal respident="response1">3330</varequal>
                <not>
                  <varequal respident="response1">9158</varequal>
                </not>
                <not>
                  <varequal respident="response1">9999</varequal>
                </not>
              </and>
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>"""
  with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','a') as f:
    f.write(multiple_choice_question)
  return id

def add_text_only_question_beta(id=id,information=""):
    id += 1
    text_only_question = f"""<item ident=\"{id}\" title=\"Question\">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>text_only_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>0.0</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>original_answer_ids</fieldlabel>
              <fieldentry></fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>gf47b767d37e06559ff801f2d253307ba</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype=\"text/html\">{information}</mattext>
          </material>
        </presentation>
      </item>"""
    with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','a') as f:
      f.write(text_only_question)
    return id

def add_general_header(id=id,information=""):
    id += 1
    text_only_question = f"""<item ident=\"{id}\" title=\"Question\">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>text_only_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>0.0</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>original_answer_ids</fieldlabel>
              <fieldentry></fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>gf47b767d37e06559ff801f2d253307ba</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype=\"text/html\">&lt;h4 style=\"color: #d0111a;\"&gt;{information}&lt;/h4&gt;</mattext>
          </material>
        </presentation>
      </item>"""
    with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','a') as f:
      f.write(text_only_question)
    return id

def add_file_upload_question(id=id,points=5.0,text_for_students="&lt;div&gt;Upload your recording here.&lt;/div&gt;"):
    id += 1
    file_upload_question = f"""<item ident="{id}" title="Question">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>file_upload_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>{points}</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>original_answer_ids</fieldlabel>
              <fieldentry></fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>gf47b767d37e06559ff801f2d253307ba</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">{text_for_students}</mattext>
          </material>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
        </resprocessing>
      </item>"""
    with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','a') as f:
      f.write(file_upload_question)
def add_essay_question(id=id,points=1.0,text_for_students="Write your answer here."):
    '''This is verified it works.'''
    id += 1
    essay_question = f"""<item ident=\"{id}\" title=\"Question\">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>essay_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>{points}</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>original_answer_ids</fieldlabel>
              <fieldentry></fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>g453f4b2faebfc2d14347df88a5d8bea0</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype=\"text/html\">{text_for_students}</mattext>
          </material>
          <response_str ident=\"response1\" rcardinality=\"Single\">
            <render_fib>
              <response_label ident=\"answer1\" rshuffle=\"No\"/>
            </render_fib>
          </response_str>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue=\"100\" minvalue=\"0\" varname=\"SCORE\" vartype=\"Decimal\"/>
          </outcomes>
          <respcondition continue=\"No\">
            <conditionvar>
              <other/>
            </conditionvar>
          </respcondition>
        </resprocessing>
      </item>"""
    with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','a') as f:
      f.write(essay_question)
    return id
def add_the_ending():
    ending = '''</section>
  </assessment>
  </questestinterop>'''
    with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','a') as f:
      f.write(ending)
    #print(ending)
def add_a_part(id=id,number=1,instructions=""):
    id += 1
    general_header = f"""<item ident=\"{id}\" title=\"Question\">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>text_only_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>0.0</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>original_answer_ids</fieldlabel>
              <fieldentry></fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>gf47b767d37e06559ff801f2d253307ba</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype=\"text/html\">&lt;div&gt;&lt;p&gt;&lt;strong&gt;&lt;span style=\"color: #d0111a;\"&gt;Part {number}.&amp;nbsp;&lt;/span&gt;{instructions}&lt;/p&gt;
    </mattext>
          </material>
        </presentation>
      </item>"""
    with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','a') as f:
      f.write(general_header)
    return id

def add_beta_multiple_choice_question(*args,id=id,points=1.0,instruction="&lt;p&gt;Select the correct answer.&lt;/p&gt;",correct=0):
  id += 1
  correct = [5530,3030,5648,9898,73][correct]
  answers = list(args)
  field_entries = ""
  for i in range(len(answers)):
    if (i + 1) == len(answers):
      field_entries += str(i)
    else:
      field_entries += str(i) + ","
  args = sorted(list(args))
  multiple_choice_question = f"""<item ident=\"{id}\" title="Question">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>multiple_choice_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>1.0</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>original_answer_ids</fieldlabel>
              <fieldentry>5530,3030,5648,9898,73</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>gd87f0e523dfee1062d7e6c5dc959c658</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">&lt;div&gt;&lt;p&gt;{instruction}&lt;/p&gt;&lt;/div&gt;</mattext>
          </material>
          <response_lid ident="response1" rcardinality="Single">
            <render_choice>
              <response_label ident="5530">
                <material>
                  <mattext texttype="text/plain">{args[0]}</mattext>
                </material>
              </response_label>
              <response_label ident="3030">
                <material>
                  <mattext texttype="text/plain">{args[1]}</mattext>
                </material>
              </response_label>
              <response_label ident="5648">
                <material>
                  <mattext texttype="text/plain">{args[2]}</mattext>
                </material>
              </response_label>
              <response_label ident="9898">
                <material>
                  <mattext texttype="text/plain">{args[3]}</mattext>
                </material>
              </response_label>
              <response_label ident="73">
                <material>
                  <mattext texttype="text/plain">{args[4]}</mattext>
                </material>
              </response_label>
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
          <respcondition continue="No">
            <conditionvar>
              <varequal respident="response1">5530</varequal>
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>"""
  with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','a') as f:
    f.write(multiple_choice_question)
  return id

def add_multiple_choice_question(*args,id=id,points=1.0,instruction="&lt;p&gt;Select the correct answer.&lt;/p&gt;",correct=""):
  id += 1
  answers = list(args)
  field_entries = ""
  for i in range(len(answers)):
    if (i + 1) == len(answers):
      field_entries += str(i)
    else:
      field_entries += str(i) + ","
  args = sorted(list(args))
  multiple_choice_question = f"""<item ident=\"{id}\" title="Question">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>multiple_choice_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>1.0</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>original_answer_ids</fieldlabel>
              <fieldentry>5530,3030,5648,9898,73</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>gd87f0e523dfee1062d7e6c5dc959c658</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">&lt;div&gt;&lt;p&gt;{instruction}&lt;/p&gt;&lt;/div&gt;</mattext>
          </material>
          <response_lid ident="response1" rcardinality="Single">
            <render_choice>
              <response_label ident="5530">
                <material>
                  <mattext texttype="text/plain">{args[0]}</mattext>
                </material>
              </response_label>
              <response_label ident="3030">
                <material>
                  <mattext texttype="text/plain">{args[1]}</mattext>
                </material>
              </response_label>
              <response_label ident="5648">
                <material>
                  <mattext texttype="text/plain">{args[2]}</mattext>
                </material>
              </response_label>
              <response_label ident="9898">
                <material>
                  <mattext texttype="text/plain">{args[3]}</mattext>
                </material>
              </response_label>
              <response_label ident="73">
                <material>
                  <mattext texttype="text/plain">{args[4]}</mattext>
                </material>
              </response_label>
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
          <respcondition continue="No">
            <conditionvar>
              <varequal respident="response1">5530</varequal>
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>"""
  with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','a') as f:
    f.write(multiple_choice_question)

def add_multiple_choice_question_beta(*args,id=id,points=1.0,instruction="&lt;p&gt;Select the correct answer.&lt;/p&gt;",correct=""):
  print("hi")
  id += 1
  print(id)
  answers = list(args)
  field_entries = ""
  for i in range(len(answers)):
    if (i + 1) == len(answers):
      field_entries += str(i)
    else:
      field_entries += str(i) + ","
  args = sorted(list(args))
  multiple_choice_question = f"""<item ident=\"{id}\" title="Question">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>multiple_choice_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>1.0</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>original_answer_ids</fieldlabel>
              <fieldentry>5530,3030,5648,9898,73</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>gd87f0e523dfee1062d7e6c5dc959c658</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">&lt;div&gt;&lt;p&gt;{instruction}&lt;/p&gt;&lt;/div&gt;</mattext>
          </material>
          <response_lid ident="response1" rcardinality="Single">
            <render_choice>
              <response_label ident="5530">
                <material>
                  <mattext texttype="text/plain">{args[0]}</mattext>
                </material>
              </response_label>
              <response_label ident="3030">
                <material>
                  <mattext texttype="text/plain">{args[1]}</mattext>
                </material>
              </response_label>
              <response_label ident="5648">
                <material>
                  <mattext texttype="text/plain">{args[2]}</mattext>
                </material>
              </response_label>
              <response_label ident="9898">
                <material>
                  <mattext texttype="text/plain">{args[3]}</mattext>
                </material>
              </response_label>
              <response_label ident="73">
                <material>
                  <mattext texttype="text/plain">{args[4]}</mattext>
                </material>
              </response_label>
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
          <respcondition continue="No">
            <conditionvar>
              <varequal respident="response1">5530</varequal>
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>"""
  with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','a') as f:
    f.write(multiple_choice_question)
  return id

def add_multiple_answer_question_beta(*args,id=id,points=1.0,instruction="&lt;p&gt;Select the correct answer.&lt;/p&gt;",correct=[0]):
  id += 1
  args = list(args)

  #Prepare possibilities part of xml
  multiple_answers_ids = ",".join(map(lambda x: str(x),list(range(len(args)))))

  #Prepare correct answer part of xml
  correct = list(map(lambda x: str(x), correct))
  correct_answers = ""
  print(correct)
  for i in range(len(args)):
    if str(i) in correct:
      correct_answers = correct_answers + f"<varequal respident=\"response1\">{i}</varequal>"
    else:
      correct_answers = correct_answers + f"""<not>
                  <varequal respident="response1">{i}</varequal>
                </not>""" 
         
  instruction = re.sub(r"[^A-z\. ]","",instruction)
  multiple_choice_question = f"""<item ident=\"q{id}\" title="Question">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>multiple_answers_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>1.0</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>original_answer_ids</fieldlabel>
              <fieldentry>{multiple_answers_ids}</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>g1c14a88a7d09754b38e6a6b464694651</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">{instruction}</mattext>
          </material>
          <response_lid ident="response1" rcardinality="Multiple">
            <render_choice>
              <response_label ident="0">
                <material>
                  <mattext texttype="text/plain">{args[0]}</mattext>
                </material>
              </response_label>
              <response_label ident="1">
                <material>
                  <mattext texttype="text/plain">{args[1]}</mattext>
                </material>
              </response_label>
              <response_label ident="2">
                <material>
                  <mattext texttype="text/plain">{args[2]}</mattext>
                </material>
              </response_label>
              <response_label ident="3">
                <material>
                  <mattext texttype="text/plain">{args[3]}</mattext>
                </material>
              </response_label>
              <response_label ident="4">
                <material>
                  <mattext texttype="text/plain">{args[4]}</mattext>
                </material>
              </response_label>
               <response_label ident="5">
                <material>
                  <mattext texttype="text/plain">{args[5]}</mattext>
                </material>
              </response_label>
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
          <respcondition continue="No">
            <conditionvar>
              <and>
                {correct_answers}
              </and>
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>"""
  with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','a') as f:
    f.write(multiple_choice_question)
  return id

def add_multiple_answer_question(*args,id=id,points=1.0,instruction="&lt;p&gt;Select the correct answer.&lt;/p&gt;",correct=""):
  id += 1
  answers = list(args)
  field_entries = ""
  for i in range(len(answers)):
    if (i + 1) == len(answers):
      field_entries += str(i)
    else:
      field_entries += str(i) + ","
  args = sorted(list(args))
  multiple_choice_question = f"""<item ident=\"{id}\" title="Question">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>multiple_answers_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>1.0</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>original_answer_ids</fieldlabel>
              <fieldentry>331,9681,7567,3330,9158,9999</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>g1c14a88a7d09754b38e6a6b464694651</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">&lt;div&gt;&lt;p&gt;REPLACE ME&lt;/p&gt;&lt;/div&gt;</mattext>
          </material>
          <response_lid ident="response1" rcardinality="Multiple">
            <render_choice>
              <response_label ident="331">
                <material>
                  <mattext texttype="text/plain">{args[0]}</mattext>
                </material>
              </response_label>
              <response_label ident="9681">
                <material>
                  <mattext texttype="text/plain">{args[1]}</mattext>
                </material>
              </response_label>
              <response_label ident="7567">
                <material>
                  <mattext texttype="text/plain">{args[2]}</mattext>
                </material>
              </response_label>
              <response_label ident="3330">
                <material>
                  <mattext texttype="text/plain">{args[3]}</mattext>
                </material>
              </response_label>
              <response_label ident="9158">
                <material>
                  <mattext texttype="text/plain">{args[4]}</mattext>
                </material>
              </response_label>
               <response_label ident="9999">
                <material>
                  <mattext texttype="text/plain">{args[5]}</mattext>
                </material>
              </response_label>
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
          <respcondition continue="No">
            <conditionvar>
              <and>
                <not>
                <varequal respident="response1">331</varequal>
                </not>
                <not>
                  <varequal respident="response1">9681</varequal>
                </not>
                <not>
                  <varequal respident="response1">7567</varequal>
                </not>
                <varequal respident="response1">3330</varequal>
                <not>
                  <varequal respident="response1">9158</varequal>
                </not>
                <not>
                  <varequal respident="response1">9999</varequal>
                </not>
              </and>
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>"""
  with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','a') as f:
    f.write(multiple_choice_question)
  return id

def add_true_false_question(id=id,points=1.0,instruction="&lt;p&gt;I am true.&lt;/p&gt;",correct=True):
  id += 1
  if correct == True:
    response_value = 6630
  else:
    response_value = 6539
  true_false_question = f"""<item ident=\"{id}\" title=\"Question\">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>true_false_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>1.0</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>original_answer_ids</fieldlabel>
              <fieldentry>6630,6539</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>g5682c619429cc8ffa7eb66581fc39df5</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype=\"text/html\">&lt;div&gt;&lt;p&gt;{instruction}&lt;/p&gt;&lt;/div&gt;</mattext>
          </material>
          <response_lid ident=\"response1\" rcardinality=\"Single\">
            <render_choice>
              <response_label ident=\"6630\">
                <material>
                  <mattext texttype=\"text/plain\">True</mattext>
                </material>
              </response_label>
              <response_label ident=\"6539\">
                <material>
                  <mattext texttype=\"text/plain\">False</mattext>
                </material>
              </response_label>
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue=\"100\" minvalue=\"0\" varname=\"SCORE\" vartype=\"Decimal\"/>
          </outcomes>
          <respcondition continue=\"No\">
            <conditionvar>
              <varequal respident=\"response1\">{response_value}</varequal>
            </conditionvar>
            <setvar action=\"Set\" varname=\"SCORE\">100</setvar>
          </respcondition>
        </resprocessing>
      </item>"""
  with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','a') as f:
    f.write(true_false_question)

def add_matching_question(id=id,points=1.0,instruction="",correct="",**kwargs):
  answer_choices = """<render_choice>"""
  ids_for_definitions = {}
  for i, key in enumerate(kwargs):
    ids_for_definitions[kwargs[key]] = "5000" + str(i)
    answer_choices += f"""<response_label ident=\"{"5000" + str(i)}\">
                <material>
                  <mattext>{kwargs[key]}</mattext>
                </material>
              </response_label>"""
  answer_choices += """</render_choice>
          </response_lid>"""
  
  ids_for_terms = {}
  list_of_ids = ""
  for i, key in enumerate(kwargs):
    ids_for_terms[key] = "7000" + str(i)
    if (i + 1) == len(kwargs):
      list_of_ids += ids_for_terms[key]
    else:
      list_of_ids += ids_for_terms[key] + ","

  matching_question = f"""<item ident=\"{id}\" title=\"Question\">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>matching_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>1.0</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>original_answer_ids</fieldlabel>
              <fieldentry>{list_of_ids}</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>g9295ef4ef1981f606d2ee83ee773a1f7</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype=\"text/html\">&lt;div&gt;&lt;/div&gt;</mattext>
          </material>"""
  for key in kwargs:
    matching_question += f"""<response_lid ident=\"response_{ids_for_terms[key]}\">
            <material>
              <mattext texttype=\"text/plain\">{key}</mattext>
            </material>"""
    matching_question += answer_choices + "</response_lid>"

  matching_question += """            
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue=\"100\" minvalue=\"0\" varname=\"SCORE\" vartype=\"Decimal\"/>
          </outcomes>"""
  for key in kwargs:
    matching_question += f"""
          <respcondition>
            <conditionvar>
              <varequal respident=\"response_{ids_for_terms[key]}\">{ids_for_definitions[kwargs[key]]}</varequal>
            </conditionvar>
            <setvar varname=\"SCORE\" action=\"Add\">{100.00/float(len(kwargs))}</setvar>
          </respcondition>"""
          
  matching_question += """
        </resprocessing>
      </item>"""
  with open('C:\\Users\\User\\Documents\\Curriculum Development\\Create Canvas Assignments Quickly\\zip_and_upload_to_Canvas\\ge5319f015006e41be4bbf9e8c7d3e89a\\ge5319f015006e41be4bbf9e8c7d3e89a.xml','a') as f:
      f.write(matching_question)

def create_array_worth_of_fill_in_the_multiple_choice_questions(array,id,correct_answers=[]):
  for i, x in enumerate(array):
    if i >= len(correct_answers):
      correct_answer = "a"
    else:
      correct_answer = correct_answers[i]
    id += 1
    add_multiple_choice_question(correct_answer,"b","c","d",id=id,points=1.0,instruction=x,correct=correct_answer)
    return id
  
def create_array_worth_of_fill_in_the_blank_questions_essay_version(array,id):
  for i, _ in enumerate(array):
    id += 1
    add_essay_question(id=id,points=1.0,text_for_students=array[i][0])
  return id
