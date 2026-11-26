#
# PySNMP MIB module CISCO-L4L7MODULE-REDUNDANCY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-L4L7MODULE-REDUNDANCY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
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
ciscoL4l7moduleRedundancyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 566))
ciscoL4l7moduleRedundancyCapability.setRevisions(('2008-07-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setRevisionsDescriptions(('Added capability statement cl4l7ModRedCapc4701aceVA3R100',))
if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setLastUpdated('200807230000Z')
if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setContactInfo('Cisco Systems\n            Customer Service\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-l4l7security@cisco.com')
if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setDescription('The capabilities description for\n        CISCO-L4L7MODULE-REDUNDANCY-MIB.')
cl4l7ModRedCapc4710aceVA3R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 566, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cl4l7ModRedCapc4710aceVA3R100 = cl4l7ModRedCapc4710aceVA3R100.setProductRelease('ACSW (Application Control Software) A3(1) for\n                     ACE 4710 Application Control Engine Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cl4l7ModRedCapc4710aceVA3R100 = cl4l7ModRedCapc4710aceVA3R100.setStatus('current')
if mibBuilder.loadTexts: cl4l7ModRedCapc4710aceVA3R100.setDescription('CISCO-L4L7-MODULE-REDUNDANCY-MIB capabilities')
mibBuilder.exportSymbols("CISCO-L4L7MODULE-REDUNDANCY-CAPABILITY", ciscoL4l7moduleRedundancyCapability=ciscoL4l7moduleRedundancyCapability, PYSNMP_MODULE_ID=ciscoL4l7moduleRedundancyCapability, cl4l7ModRedCapc4710aceVA3R100=cl4l7ModRedCapc4710aceVA3R100)
