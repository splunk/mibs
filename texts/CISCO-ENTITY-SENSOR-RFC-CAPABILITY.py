#
# PySNMP MIB module CISCO-ENTITY-SENSOR-RFC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENTITY-SENSOR-RFC-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoEntitySensorRfcCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 430))
ciscoEntitySensorRfcCapability.setRevisions(('2008-02-08 00:00', '2006-05-31 00:00', '2005-01-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntitySensorRfcCapability.setRevisionsDescriptions(('Added cEntSensorRfcCapc4710aceVA1R70\n        agent capabilities for ACE 4710 Application \n        Control Engine Appliance.', 'Added cEntSensorRfcCapACSWV03R000 for\n        Application Control Engine(ACE) Service \n        Module.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntitySensorRfcCapability.setLastUpdated('200802080000Z')
if mibBuilder.loadTexts: ciscoEntitySensorRfcCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntitySensorRfcCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com,\n            cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntitySensorRfcCapability.setDescription('The capabilities description of\n        ENTITY-SENSOR-MIB.')
cEntSensorRfcCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 430, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapCatOSV08R0501 = cEntSensorRfcCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapCatOSV08R0501 = cEntSensorRfcCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: cEntSensorRfcCapCatOSV08R0501.setDescription('ENTITY-SENSOR-MIB capabilities.')
cEntSensorRfcCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 430, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapACSWV03R000 = cEntSensorRfcCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                    for Application Control Engine(ACE) \n                    Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapACSWV03R000 = cEntSensorRfcCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: cEntSensorRfcCapACSWV03R000.setDescription('ENTITY-SENSOR-MIB capabilities.')
cEntSensorRfcCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 430, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapc4710aceVA1R70 = cEntSensorRfcCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapc4710aceVA1R70 = cEntSensorRfcCapc4710aceVA1R70.setStatus('current')
if mibBuilder.loadTexts: cEntSensorRfcCapc4710aceVA1R70.setDescription('ENTITY-SENSOR-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-RFC-CAPABILITY", cEntSensorRfcCapc4710aceVA1R70=cEntSensorRfcCapc4710aceVA1R70, PYSNMP_MODULE_ID=ciscoEntitySensorRfcCapability, ciscoEntitySensorRfcCapability=ciscoEntitySensorRfcCapability, cEntSensorRfcCapACSWV03R000=cEntSensorRfcCapACSWV03R000, cEntSensorRfcCapCatOSV08R0501=cEntSensorRfcCapCatOSV08R0501)
