#
# PySNMP MIB module CISCO-ENTITY-SENSOR-RFC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENTITY-SENSOR-RFC-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntitySensorRfcCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 430))
ciscoEntitySensorRfcCapability.setRevisions(('2008-02-08 00:00', '2006-05-31 00:00', '2005-01-31 00:00',))
if mibBuilder.loadTexts: ciscoEntitySensorRfcCapability.setLastUpdated('200802080000Z')
if mibBuilder.loadTexts: ciscoEntitySensorRfcCapability.setOrganization('Cisco Systems, Inc.')
cEntSensorRfcCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 430, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapCatOSV08R0501 = cEntSensorRfcCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapCatOSV08R0501 = cEntSensorRfcCapCatOSV08R0501.setStatus('current')
cEntSensorRfcCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 430, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapACSWV03R000 = cEntSensorRfcCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                    for Application Control Engine(ACE) \n                    Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapACSWV03R000 = cEntSensorRfcCapACSWV03R000.setStatus('current')
cEntSensorRfcCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 430, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapc4710aceVA1R70 = cEntSensorRfcCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapc4710aceVA1R70 = cEntSensorRfcCapc4710aceVA1R70.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-RFC-CAPABILITY", cEntSensorRfcCapc4710aceVA1R70=cEntSensorRfcCapc4710aceVA1R70, cEntSensorRfcCapACSWV03R000=cEntSensorRfcCapACSWV03R000, ciscoEntitySensorRfcCapability=ciscoEntitySensorRfcCapability, cEntSensorRfcCapCatOSV08R0501=cEntSensorRfcCapCatOSV08R0501, PYSNMP_MODULE_ID=ciscoEntitySensorRfcCapability)
