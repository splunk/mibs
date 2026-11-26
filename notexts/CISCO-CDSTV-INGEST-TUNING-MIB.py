#
# PySNMP MIB module CISCO-CDSTV-INGEST-TUNING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CDSTV-INGEST-TUNING-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCdstvIngestTuningMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 750))
ciscoCdstvIngestTuningMIB.setRevisions(('2010-06-24 00:00',))
if mibBuilder.loadTexts: ciscoCdstvIngestTuningMIB.setLastUpdated('201006240000Z')
if mibBuilder.loadTexts: ciscoCdstvIngestTuningMIB.setOrganization('Cisco Systems, Inc.')
ciscoCdstvIngestTuningMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 0))
ciscoCdstvIngestTuningMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 1))
ciscoCdstvIngestTuningMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 2))
ciscoCdstvIngestTuningMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 1))
cdstvTrickModeSpeedTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1), )
if mibBuilder.loadTexts: cdstvTrickModeSpeedTable.setStatus('current')
cdstvTrickModeSpeedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1, 1), ).setIndexNames((0, "CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvTrickModeSpeedIndex"))
if mibBuilder.loadTexts: cdstvTrickModeSpeedEntry.setStatus('current')
cdstvTrickModeSpeedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cdstvTrickModeSpeedIndex.setStatus('current')
cdstvTrickModeSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-127, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvTrickModeSpeed.setStatus('current')
cdstvServerIngestMPEGSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2))
cdstvServerPIDStandardization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerPIDStandardization.setStatus('current')
cdstvServerSequenceEndRemove = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerSequenceEndRemove.setStatus('current')
cdstvServerRateStandardize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerRateStandardize.setStatus('current')
ciscoCdstvIngestTuningMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 2))
ciscoCdstvIngestTuningMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 1, 1)).setObjects(("CISCO-CDSTV-INGEST-TUNING-MIB", "ciscoCdstvIngestTuningMIBMainObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvIngestTuningMIBCompliance = ciscoCdstvIngestTuningMIBCompliance.setStatus('current')
ciscoCdstvIngestTuningMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 2, 1)).setObjects(("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvTrickModeSpeed"), ("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvServerPIDStandardization"), ("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvServerSequenceEndRemove"), ("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvServerRateStandardize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvIngestTuningMIBMainObjectGroup = ciscoCdstvIngestTuningMIBMainObjectGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CDSTV-INGEST-TUNING-MIB", ciscoCdstvIngestTuningMIB=ciscoCdstvIngestTuningMIB, ciscoCdstvIngestTuningMIBGroups=ciscoCdstvIngestTuningMIBGroups, cdstvServerIngestMPEGSettings=cdstvServerIngestMPEGSettings, cdstvServerRateStandardize=cdstvServerRateStandardize, PYSNMP_MODULE_ID=ciscoCdstvIngestTuningMIB, cdstvTrickModeSpeed=cdstvTrickModeSpeed, cdstvServerSequenceEndRemove=cdstvServerSequenceEndRemove, ciscoCdstvIngestTuningMIBConform=ciscoCdstvIngestTuningMIBConform, ciscoCdstvIngestTuningMIBCompliances=ciscoCdstvIngestTuningMIBCompliances, cdstvServerPIDStandardization=cdstvServerPIDStandardization, ciscoCdstvIngestTuningMIBMainObjectGroup=ciscoCdstvIngestTuningMIBMainObjectGroup, ciscoCdstvIngestTuningMIBCompliance=ciscoCdstvIngestTuningMIBCompliance, ciscoCdstvIngestTuningMIBNotifs=ciscoCdstvIngestTuningMIBNotifs, cdstvTrickModeSpeedIndex=cdstvTrickModeSpeedIndex, ciscoCdstvIngestTuningMIBObjects=ciscoCdstvIngestTuningMIBObjects, cdstvTrickModeSpeedEntry=cdstvTrickModeSpeedEntry, cdstvTrickModeSpeedTable=cdstvTrickModeSpeedTable)
