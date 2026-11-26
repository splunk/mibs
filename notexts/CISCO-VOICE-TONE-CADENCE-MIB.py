#
# PySNMP MIB module CISCO-VOICE-TONE-CADENCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-TONE-CADENCE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cmgwIndex, CVoiceTonePlanIndex = mibBuilder.importSymbols("CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex", "CVoiceTonePlanIndex")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CountryCode, = mibBuilder.importSymbols("CISCO-TC", "CountryCode")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention, RowStatus, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "StorageType")
ciscoVoiceToneCadenceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 356))
ciscoVoiceToneCadenceMIB.setRevisions(('2003-05-28 00:00',))
if mibBuilder.loadTexts: ciscoVoiceToneCadenceMIB.setLastUpdated('200305280000Z')
if mibBuilder.loadTexts: ciscoVoiceToneCadenceMIB.setOrganization('Cisco Systems, Inc.')
ciscoVoiceToneCadenceMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 356, 0))
ciscoVoiceToneCadenceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 356, 1))
cVoiceToneCadenceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1))
class CToneFrequency(TextualConvention, OctetString):
    reference = 'ITU E.180 Supplement 2 - Various Tones Used In National Network.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class CToneAmplitude(TextualConvention, OctetString):
    reference = 'ITU E.180/Q.35 - Technical Characteristic of Tones for the Telephone Service.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 64)

class CToneCadence(TextualConvention, OctetString):
    reference = 'ITU E.180 Supplement 2 - Various Tones Used In National Network.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 64)

cvtcTonePlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1), )
if mibBuilder.loadTexts: cvtcTonePlanTable.setStatus('current')
cvtcTonePlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"), (0, "CISCO-VOICE-TONE-CADENCE-MIB", "cvtcTonePlanId"))
if mibBuilder.loadTexts: cvtcTonePlanEntry.setStatus('current')
cvtcTonePlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1, 1, 1), CVoiceTonePlanIndex())
if mibBuilder.loadTexts: cvtcTonePlanId.setStatus('current')
cvtcTonePlanVifCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvtcTonePlanVifCount.setStatus('current')
cvtcTonePlanCountry = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1, 1, 3), CountryCode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtcTonePlanCountry.setStatus('current')
cvtcTonePlanVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtcTonePlanVersion.setStatus('current')
cvtcTonePlanFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtcTonePlanFileName.setStatus('current')
cvtcTonePlanStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1, 1, 6), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvtcTonePlanStorageType.setStatus('current')
cvtcTonePlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtcTonePlanRowStatus.setStatus('current')
cvtcToneIdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 2), )
if mibBuilder.loadTexts: cvtcToneIdTable.setStatus('current')
cvtcToneIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"), (0, "CISCO-VOICE-TONE-CADENCE-MIB", "cvtcToneId"))
if mibBuilder.loadTexts: cvtcToneIdEntry.setStatus('current')
cvtcToneId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cvtcToneId.setStatus('current')
cvtcToneName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtcToneName.setStatus('current')
cvtcToneIdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtcToneIdRowStatus.setStatus('current')
cvtcProgrammableToneTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 3), )
if mibBuilder.loadTexts: cvtcProgrammableToneTable.setStatus('current')
cvtcProgrammableToneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"), (0, "CISCO-VOICE-TONE-CADENCE-MIB", "cvtcTonePlanId"), (0, "CISCO-VOICE-TONE-CADENCE-MIB", "cvtcToneId"))
if mibBuilder.loadTexts: cvtcProgrammableToneEntry.setStatus('current')
cvtcProgrammableToneFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 3, 1, 1), CToneFrequency()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtcProgrammableToneFrequency.setStatus('current')
cvtcProgrammableToneAmplitude = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 3, 1, 2), CToneAmplitude()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtcProgrammableToneAmplitude.setStatus('current')
cvtcProgrammableToneCadence = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 3, 1, 3), CToneCadence()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtcProgrammableToneCadence.setStatus('current')
cvtcProgrammableToneDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtcProgrammableToneDuration.setStatus('current')
cvtcProgrammableToneStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 3, 1, 5), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtcProgrammableToneStorageType.setStatus('current')
cvtcProgrammableToneRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtcProgrammableToneRowStatus.setStatus('current')
ciscoVoiceToneCadenceMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 356, 3))
cVoiceToneCadenceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 356, 3, 1))
cVoiceToneCadenceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 356, 3, 2))
cVoiceToneCadenceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 356, 3, 1, 1)).setObjects(("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcToneConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceToneCadenceCompliance = cVoiceToneCadenceCompliance.setStatus('current')
cvtcToneConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 356, 3, 2, 1)).setObjects(("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcTonePlanVifCount"), ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcTonePlanCountry"), ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcTonePlanVersion"), ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcTonePlanFileName"), ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcTonePlanStorageType"), ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcTonePlanRowStatus"), ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcToneName"), ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcToneIdRowStatus"), ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcProgrammableToneFrequency"), ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcProgrammableToneAmplitude"), ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcProgrammableToneCadence"), ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcProgrammableToneDuration"), ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcProgrammableToneStorageType"), ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcProgrammableToneRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvtcToneConfigGroup = cvtcToneConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-TONE-CADENCE-MIB", cvtcTonePlanFileName=cvtcTonePlanFileName, cvtcToneName=cvtcToneName, cvtcProgrammableToneStorageType=cvtcProgrammableToneStorageType, cvtcProgrammableToneRowStatus=cvtcProgrammableToneRowStatus, cvtcTonePlanRowStatus=cvtcTonePlanRowStatus, cvtcTonePlanId=cvtcTonePlanId, ciscoVoiceToneCadenceMIBConform=ciscoVoiceToneCadenceMIBConform, cvtcProgrammableToneEntry=cvtcProgrammableToneEntry, cvtcTonePlanVersion=cvtcTonePlanVersion, cVoiceToneCadenceCompliance=cVoiceToneCadenceCompliance, cvtcProgrammableToneAmplitude=cvtcProgrammableToneAmplitude, cvtcTonePlanCountry=cvtcTonePlanCountry, ciscoVoiceToneCadenceMIBObjects=ciscoVoiceToneCadenceMIBObjects, CToneFrequency=CToneFrequency, ciscoVoiceToneCadenceMIBNotifs=ciscoVoiceToneCadenceMIBNotifs, cVoiceToneCadenceGroups=cVoiceToneCadenceGroups, CToneCadence=CToneCadence, cvtcProgrammableToneDuration=cvtcProgrammableToneDuration, cvtcToneIdTable=cvtcToneIdTable, cvtcTonePlanStorageType=cvtcTonePlanStorageType, cvtcToneId=cvtcToneId, cVoiceToneCadenceConfig=cVoiceToneCadenceConfig, cvtcToneIdEntry=cvtcToneIdEntry, cVoiceToneCadenceCompliances=cVoiceToneCadenceCompliances, cvtcTonePlanTable=cvtcTonePlanTable, ciscoVoiceToneCadenceMIB=ciscoVoiceToneCadenceMIB, cvtcToneConfigGroup=cvtcToneConfigGroup, cvtcToneIdRowStatus=cvtcToneIdRowStatus, cvtcProgrammableToneFrequency=cvtcProgrammableToneFrequency, CToneAmplitude=CToneAmplitude, cvtcProgrammableToneTable=cvtcProgrammableToneTable, cvtcTonePlanVifCount=cvtcTonePlanVifCount, PYSNMP_MODULE_ID=ciscoVoiceToneCadenceMIB, cvtcProgrammableToneCadence=cvtcProgrammableToneCadence, cvtcTonePlanEntry=cvtcTonePlanEntry)
