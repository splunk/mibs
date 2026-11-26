#
# PySNMP MIB module CISCO-SLB-HEALTH-MON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SLB-HEALTH-MON-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
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
ciscoSlbHealthMonCapapbility = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 508))
ciscoSlbHealthMonCapapbility.setRevisions(('2008-07-03 00:00', '2008-02-08 00:00', '2006-06-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setRevisionsDescriptions(('Added ciscoSlbHealthMonCapc4710aceVA3R100\n        agent capabilities for ACE 4710 Application \n        Control Engine Appliance.', 'Added ciscoSlbHealthMonCapc4710aceVA1R700\n        agent capabilities for ACE 4710 Application \n        Control Engine Appliance.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setLastUpdated('200807030000Z')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setDescription('The capabilities description of\n        CISCO-SLB-HEALTH-MON-MIB.')
ciscoSlbHealthMonCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 508, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapabilityACSWV03R000 = ciscoSlbHealthMonCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapabilityACSWV03R000 = ciscoSlbHealthMonCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapabilityACSWV03R000.setDescription('CISCO-SLB-HEALTH-MON-MIB capabilities.')
ciscoSlbHealthMonCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 508, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapc4710aceVA1R700 = ciscoSlbHealthMonCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                for ACE 4710 Application Control Engine \n                Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapc4710aceVA1R700 = ciscoSlbHealthMonCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapc4710aceVA1R700.setDescription('CISCO-SLB-HEALTH-MON-MIB capabilities.')
ciscoSlbHealthMonCapc4710aceVA3R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 508, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapc4710aceVA3R100 = ciscoSlbHealthMonCapc4710aceVA3R100.setProductRelease('ACSW (Application Control Software) A3(1.0)\n                for ACE 4710 Application Control Engine \n                Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapc4710aceVA3R100 = ciscoSlbHealthMonCapc4710aceVA3R100.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapc4710aceVA3R100.setDescription('CISCO-SLB-HEALTH-MON-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SLB-HEALTH-MON-CAPABILITY", ciscoSlbHealthMonCapc4710aceVA1R700=ciscoSlbHealthMonCapc4710aceVA1R700, ciscoSlbHealthMonCapabilityACSWV03R000=ciscoSlbHealthMonCapabilityACSWV03R000, ciscoSlbHealthMonCapapbility=ciscoSlbHealthMonCapapbility, ciscoSlbHealthMonCapc4710aceVA3R100=ciscoSlbHealthMonCapc4710aceVA3R100, PYSNMP_MODULE_ID=ciscoSlbHealthMonCapapbility)
