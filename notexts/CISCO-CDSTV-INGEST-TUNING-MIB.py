#
# PySNMP MIB module CISCO-CDSTV-INGEST-TUNING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CDSTV-INGEST-TUNING-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32")
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
mibBuilder.exportSymbols("CISCO-CDSTV-INGEST-TUNING-MIB", cdstvTrickModeSpeedEntry=cdstvTrickModeSpeedEntry, PYSNMP_MODULE_ID=ciscoCdstvIngestTuningMIB, ciscoCdstvIngestTuningMIBNotifs=ciscoCdstvIngestTuningMIBNotifs, cdstvServerRateStandardize=cdstvServerRateStandardize, cdstvServerPIDStandardization=cdstvServerPIDStandardization, ciscoCdstvIngestTuningMIBConform=ciscoCdstvIngestTuningMIBConform, cdstvTrickModeSpeedTable=cdstvTrickModeSpeedTable, ciscoCdstvIngestTuningMIBCompliance=ciscoCdstvIngestTuningMIBCompliance, ciscoCdstvIngestTuningMIBCompliances=ciscoCdstvIngestTuningMIBCompliances, ciscoCdstvIngestTuningMIBObjects=ciscoCdstvIngestTuningMIBObjects, cdstvServerSequenceEndRemove=cdstvServerSequenceEndRemove, ciscoCdstvIngestTuningMIBMainObjectGroup=ciscoCdstvIngestTuningMIBMainObjectGroup, cdstvTrickModeSpeed=cdstvTrickModeSpeed, cdstvServerIngestMPEGSettings=cdstvServerIngestMPEGSettings, cdstvTrickModeSpeedIndex=cdstvTrickModeSpeedIndex, ciscoCdstvIngestTuningMIBGroups=ciscoCdstvIngestTuningMIBGroups, ciscoCdstvIngestTuningMIB=ciscoCdstvIngestTuningMIB)
